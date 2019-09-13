# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import mapnik
import os
from osgeo import osr
import osgeo.ogr as ogr
from random import randint

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)



class MapnikWidget(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.map = mapnik.Map(512, 512)
        self.map.background = mapnik.Color('white')
        self.qim = QImage()
        self.startDragPos = QPoint()
        self.endDragPos   = QPoint()
        self.zoomPos      = QPoint()
        self.drag         = False
        self.scale        = False
        self.total_scale  = 1.0
        self.timer        = QTimer()
        self.setMouseTracking(True)
        self.toolMode     = 0
        self.timer.timeout.connect(self.updateMap)
        self.mapLayers={}

    def addShapeSingleSymbole(self, fName,name=None):
        if name is None:
            name=str.split(fName,".")[0]
        clr=self.randomColor()
        ds = mapnik.Shapefile(file=fName)
        lyr = mapnik.Layer(name)
        lyr.datasource = ds
        geomType=str(ds.geometry_type())

        if geomType in ["Point", "MultiPoint"]:
            s=self.singlePointStyle(mapnik.PathExpression("Icons/point.png"),0.1)
        elif geomType in ["LineString", "MultiLineString","Line"]:
            s=self.singleLineStyle(clr,0.5)
        elif geomType in ["Polygon", "MultiPolygon"]:
            s=self.singlePolyStyle(clr)
        prjFile=fName.rsplit( ".", 1 )[ 0 ]+'.prj'
        prj=self.esriprj2standards(prjFile)
        if len(self.map.layers) == 0 and prj != '':
            self.map.srs=prj

        if prj != '': lyr.srs=prj
        self.map.append_style(name,s)
        lyr.styles.append(name)
        self.map.layers.append(lyr)
        #self.mapLayers.append(self.readOgrShape(fName))
        self.mapLayers[name]=geomType
        self.map.resize(self.width(), self.height())
        return [name,clr,geomType]

    def mapLayerOrderChange(self,NewIndex):
        if len(NewIndex) == len(self.map.layers):
            OrderedLyrs=[self.map.layers[i] for i in NewIndex]
            for i in reversed(range(len(OrderedLyrs))):
                self.map.layers.__delitem__(i)
            for i in reversed(range(len(OrderedLyrs))):
                self.map.layers.append(OrderedLyrs[i])
    def readOgrShape(self,fName):
        ###
        driver = ogr.GetDriverByName('ESRI Shapefile')
        ds = driver.Open(fName,0)
        layer = ds.GetLayer()
        return layer

    def identifyOGRlayers(self,index,x,y):
        ###
        p=ogr.Geometry(ogr.wkbPoint)
        p.AddPoint(x,y)

        layer = self.mapLayers[index]
        layer.SetSpatialFilter(p)
        layer.ResetReading()
        feature=layer.GetNextFeature()
        return feature.items()


    def addShapeUnicodeSymbole(self, fName,field,name=None):
        ###
        if name is None:
            name=str.split(fName,".")[0]

        ds = mapnik.Shapefile(file=fName)
        lyr = mapnik.Layer(name)
        lyr.datasource = ds
        geomType=str(ds.geometry_type())
        feat=self.extUniqueFeatures(ds,field)
        cols=self.randomColor(len(feat))
        if geomType in ["Point", "MultiPoint"]:
            s=self.singlePointStyle()
        elif geomType in ["LineString", "MultiLineString","Line"]:
            s=self.singleLineStyle(self.randomColor())
        elif geomType in ["Polygon", "MultiPolygon"]:
            s=self.UnicodePolyStyle(field,feat,cols)
            self.map.append_style(name,s)
        lyr.styles.append(name)
        self.map.layers.append(lyr)
        self.map.resize(self.width(), self.height())
        self.map.zoom_all()


    def close_map(self):
        self.map = mapnik.Map(512, 512)
        self.map.background = mapnik.Color('white')
        self.updateMap()

    def updateMap(self):
        self.timer.stop()
        if self.drag:
            cx = int(0.5 * self.map.width)
            cy = int(0.5 * self.map.height)
            dpos = self.endDragPos - self.startDragPos
            self.map.pan(cx - dpos.x() ,cy - dpos.y())
            self.drag = False
        elif self.scale:
            ma = QMatrix()
            ma.translate(self.zoomPos.x(), self.zoomPos.y())
            ma.scale(self.total_scale, self.total_scale)
            ma.translate(-self.zoomPos.x(), -self.zoomPos.y())

            rect = ma.mapRect(QRectF(0, 0, self.map.width, self.map.height))
            env = mapnik.Envelope(rect.left(), rect.bottom(), rect.right(), rect.top())
            self.map.zoom_to_box(self.map.view_transform().backward(env))
            self.total_scale = 1.0
            self.scale       = False

        im = mapnik.Image(self.map.width, self.map.height)
        mapnik.render(self.map, im)
        self.qim.loadFromData(QByteArray(im.tostring('png')))
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        if self.drag:
            if self.toolMode == 3:
                painter.drawImage(self.endDragPos - self.startDragPos, self.qim)
            if self.toolMode == 1:
                w=self.endDragPos.x() - self.startDragPos.x()
                h=self.endDragPos.y() - self.startDragPos.y()
                qr=QRect(self.startDragPos.x(),self.startDragPos.y(),w,h)
                painter.drawImage(0, 0, self.qim)
                painter.drawRect(qr)
            if self.toolMode == 2:
                w=self.endDragPos.x() - self.startDragPos.x()
                h=self.endDragPos.y() - self.startDragPos.y()
                qr=QRect(self.startDragPos.x(),self.startDragPos.y(),w,h)
                painter.drawImage(0, 0, self.qim)
                painter.drawRect(qr)


        elif self.scale:
            painter.save()
            scale = 1 / self.total_scale
            painter.translate(self.zoomPos.x(), self.zoomPos.y())
            painter.scale(scale, scale)
            painter.translate(-self.zoomPos.x(), -self.zoomPos.y())
            exposed = painter.matrix().inverted()[0].mapRect(self.rect()).adjusted(-1, -1, 1, 1)
            painter.drawImage(exposed, self.qim, exposed)
            painter.restore()
        else:
            painter.drawImage(0, 0, self.qim)

        painter.setPen(QColor(0, 0, 0, 100))
        painter.setBrush(QColor(0, 0, 0, 100))
        #painter.drawRect(0, 0, 256, 26)
        #painter.setPen(QColor(0, 255 , 0))
        #painter.drawText(10, 19, 'Scale Denominator: ' + str(self.map.scale_denominator()))

    def zoom_all(self):
        self.map.zoom_all()
        self.updateMap()

    def resizeEvent(self, event):
        self.map.resize(event.size().width(), event.size().height())
        self.updateMap()

    def wheelEvent(self, event):
        self.zoomPos     = event.pos()
        self.total_scale *= 1.0 - event.delta() / (360.0 * 8.0) * 4
        self.scale = True
        self.updateMap()
        self.timer.start(400)


    def mousePressEvent(self, event):
        if self.toolMode in [1,2,3]:
            if event.button() == Qt.LeftButton:
               self.startDragPos = event.pos()
               self.drag         = True
        elif self.toolMode == 4:
            try:
                r = self.parent().parent().parent().listView.currentIndex().row()


                #lyr=self.map.layers[len(self.map.layers)-1]
                lyr=self.map.layers[len(self.map.layers)-1-r]
                prjName = self.map.srs.split(' ',1)[0].split('=')[1]
                if prjName == 'longlat':
                    if str(lyr.datasource.geometry_type()) == 'Point':
                        TOL = 0.001
                    else:
                        TOL=0.001
                else:
                    if str(lyr.datasource.geometry_type()) == 'Point':
                        TOL = 0.001
                    else:
                        TOL = 0.001

            except:
                TOL = 0.01

            try:

                #if prjName == 'longlat':
                #self._prj = mapnik.Projection(self.map.layers[len(self.map.layers)-1].srs)
                #prj_trans = mapnik.ProjTransform(mapnik.Projection(self.map.srs),mapnik.Projection(self.map.layers[len(self.map.layers)-1].srs))
                #print self._prj.forward(mapnik.Coord(self.xy[0],self.xy[1]))
                #p=prj_trans.forward(mapnik.Coord(self.xy[0],self.xy[1]))
                transXY = self.xyTransform(self.xy[0],self.xy[1])
                self.xy[0]=transXY[0]
                self.xy[1]=transXY[1]

                attribXY=self.map.layers[len(self.map.layers)-1-r].datasource.features_at_point(mapnik.Coord(self.xy[0],self.xy[1]),TOL).features[0].attributes
                #attribXY=self.map.layers[len(self.map.layers)-1-r].datasource.features_at_point(mapnik.Coord(int(self.xy[0]),int(self.xy[1]))).features[0].attributes
                #attribXY=self.map.layers[len(self.map.layers)-1].datasource.features_at_point(mapnik.Coord(int(self.xy[0]),int(self.xy[1]))).features[0].attributes
                #attribXY=self.identifyOGRlayers(0,self.xy[0],self.xy[1])
##                a=[]
##                for b in attribXY.values():
##                    try:
##                        #a.append(QApplication.translate("MapnikWidget", b, None, QApplication.UnicodeUTF8))
##                        a.append(b.decode('utf-8'))
##                    except:
##                        a.append('-')
##


                #feat_model=FeatureListModel([str(b).decode('CP1256','replace') for b in attribXY.values()],attribXY.keys())
                #feat_model=FeatureListModel(a,attribXY.keys())
                feat_model=FeatureListModel(attribXY.values(),attribXY.keys())
                self.parent().parent().parent().identify.show()
                self.parent().parent().parent().identify.tableView.setModel(feat_model)
            except:
                feat_model=FeatureListModel([],[])
                self.parent().parent().parent().identify.show()

                self.parent().parent().parent().identify.tableView.setModel(feat_model)
        elif self.toolMode == 11:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            transXY = self.xyTransform(self.xy[0],self.xy[1])
            self.parent().parent().parent().x=transXY[0]
            self.parent().parent().parent().y=transXY[1]
            self.parent().parent().parent().extractData(self.parent().parent().parent().where)
            if self.parent().parent().parent().fZone:
                self.parent().parent().parent().funcZoneDialog.close()
            if self.parent().parent().parent().fRisk:
                self.parent().parent().parent().formHazardDialog.close()
            if self.parent().parent().parent().fOpt:
                self.parent().parent().parent().frmOptThreatDialog.close()
            if self.parent().parent().parent().fEcol:
                self.parent().parent().parent().formEcologicDialog.close()
            QApplication.setOverrideCursor(QCursor(Qt.WhatsThisCursor))

    def xyTransform(self,x,y):
        # transform to top layer's projection
         srcSpatialRef = osr.SpatialReference()
         srcSpatialRef.ImportFromProj4(self.map.srs)
         dstSpatialRef = osr.SpatialReference()
         dstSpatialRef.ImportFromProj4(self.map.layers[len(self.map.layers)-1].srs)
         coordTransform = osr.CoordinateTransformation(srcSpatialRef,dstSpatialRef)
         return coordTransform.TransformPoint(x,y)



    def getXY(self,pos):
        w=float(self.width())
        h = float(self.height())
        xx = pos.x() / w
        yy = (h - pos.y()) / h
        mp = self.map.envelope()
        mx=mp[2]-mp[0]
        my=mp[3]-mp[1]
        return [mx*xx+mp[0],my*yy+mp[1]]

    def mouseMoveEvent(self, event):
        self.xy= self.getXY(event.pos())
        self.parent().parent().parent().lblX.setText(str(self.xy[0]))
        self.parent().parent().parent().lblY.setText(str(self.xy[1]))
        #print self.startDragPos.x()
        if self.drag:
            if self.toolMode == 3:
                QApplication.setOverrideCursor(QCursor(Qt.ClosedHandCursor))
            self.endDragPos = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag = False
            self.endDragPos = event.pos()

            if self.toolMode == 3:
               QApplication.setOverrideCursor(QCursor(Qt.OpenHandCursor))
               cx = int(0.5 * self.map.width)
               cy = int(0.5 * self.map.height)
               dpos = self.endDragPos - self.startDragPos
               self.map.pan(cx - dpos.x() ,cy - dpos.y())
               self.updateMap()
            if self.toolMode == 1:
               env = mapnik.Envelope(self.startDragPos.x(), self.endDragPos.y(), self.endDragPos.x(), self.startDragPos.y())
               self.map.zoom_to_box(self.map.view_transform().backward(env))
               self.updateMap()
            if self.toolMode == 2:
               self.scale=True
               w=self.startDragPos.x() - self.endDragPos.x()
               h=self.startDragPos.y() - self.endDragPos.y()
               self.zoomPos = QPoint(self.endDragPos.x() + w/2,self.endDragPos.y() + h/2)
               self.total_scale *=(((self.width()/w)+(self.height()/h))/2)*0.8
               self.updateMap()

    def esriprj2standards(self,shapeprj_path):
       if os.path.exists(shapeprj_path):
           prj_file = open(shapeprj_path, 'r')
           prj_txt = prj_file.read()
           srs = osr.SpatialReference()
           srs.ImportFromESRI([prj_txt])

           return srs.ExportToProj4().strip()
       else:
            return ''
       #srs.AutoIdentifyEPSG()
       #print 'EPSG is: %s' % srs.GetAuthorityCode(None)

    def extFieldNames(self,ds):
        return ds.fields()

    def extUniqueFeatures(self,ds,field):
        f=ds.all_features([field])
        f_list=[]
        for i in range(0,len(f)):
            f_list.append(f[i].attributes[field].encode())
        return list(set(f_list))

    def UnicodePolyStyle(self,field,feats,colors):
        if len(feats) != len(colors):
            print "Error: length of fields and the specified colors should be the same!"

        polyS = mapnik.Style()
        for i in range(0,len(feats)):
            r=mapnik.Rule()
            r.filter=mapnik.Filter("["+field+"] = '"+feats[i]+"'")
            s=mapnik.PolygonSymbolizer(mapnik.Color(colors[i]))
            r.symbols.append(s)
            polyS.rules.append(r)

        r=mapnik.Rule()
        s = mapnik.LineSymbolizer(mapnik.Color("#000000"), 0.1)
        r.symbols.append(s)
        polyS.rules.append(r)
        return polyS

    def singlePolyStyle(self,clr,outlineColor="#000000",outlineThikness=0.1):
        polyS = mapnik.Style()
        r=mapnik.Rule()
        s=mapnik.PolygonSymbolizer(mapnik.Color(clr))
        r.symbols.append(s)
        polyS.rules.append(r)
        r=mapnik.Rule()
        s = mapnik.LineSymbolizer(mapnik.Color(outlineColor), outlineThikness)
        r.symbols.append(s)
        polyS.rules.append(r)
        return polyS

    def singleLineStyle(self,clr,lineThikness=0.1):
        lineS = mapnik.Style()
        r=mapnik.Rule()
        s = mapnik.LineSymbolizer(mapnik.Stroke(mapnik.Color(clr), lineThikness))
        r.symbols.append(s)
        lineS.rules.append(r)
        return lineS

    def labStyle(self,field,font="DejaVu Sans Book",size=10,clr="#000000"):
        labelStyle = mapnik.Style()
        rule = mapnik.Rule()
        symbol = mapnik.TextSymbolizer(field, font, size,mapnik.Color(clr))
        rule.symbols.append(symbol)
        labelStyle.rules.append(rule)
        return labelStyle

    def readShapeLayer(self,name,fileName):
        ds = mapnik.Shapefile(file=fileName)
        layer = mapnik.Layer(name)
        layer.datasource = ds
        return layer

    def shapeGeomType(self,fileName):
        ds = mapnik.Shapefile(file=fileName)
        return str(ds.geometry_type())

    def singlePointStyle(self,name=None,scale=0.2):
        pointS = mapnik.Style()
        r=mapnik.Rule()
        if name is not None:
            #s=mapnik.PointSymbolizer(name,"png",size,size)
            s=mapnik.PointSymbolizer(name)
        else:
            s=mapnik.PointSymbolizer()

        s.allow_overlap = True
        s.transform="scale("+str(scale)+","+str(scale)+")"
        r.symbols.append(s)
        pointS.rules.append(r)
        return pointS

    def randomColor(self,n=1):
        out=[]
        hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        for i in range(0,n):
            digit_array = []

            for i in xrange(6):
                digit_array.append(hex_digits[randint(0,15)])
            joined_digits = ''.join(digit_array)
            out.append ('#' + joined_digits)
        if n == 1:
            return out[0]
        else:
            return out


class FeatureListModel(QAbstractListModel):
    def __init__(self,FeatureAttribute=[],FieldNames=[],parent=None):
        QAbstractListModel.__init__(self,parent)
        self.__attribute=FeatureAttribute
        self.__fields=FieldNames

    def rowCount(self,parent):
        return len(self.__attribute)

    def headerData(self,section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return "Attributes"
            else:
                return self.__fields[section]

    def data(self,index,role):
        if role == Qt.DisplayRole:
            row=index.row()
            value=self.__attribute[row]
            return value

