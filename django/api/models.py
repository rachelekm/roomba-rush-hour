from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

class SidewalkManager(models.Manager):
    def get_area(self, point):
        # assuming one lane, standard 9-12 ft 
        street_width_ft = 11
        # sidewalk width does not include furnishing and building zones
        sidewalk_walking_width_ft = 6

        street_width_m = street_width_ft/3.2808
        sidewalk_walking_width_m = sidewalk_walking_width_ft/3.2808
        (lat, lng) = point.split(',')
        # get closest street to point
        closest_street = self.annotate(distance=Distance('wkb_geometry', Point(float(lng), float(lat), srid=4326))).order_by('distance').first().ogc_fid
        # get closest street's total sidewalk area
        for street in self.raw("SELECT ST_Area(ST_Difference(ST_Buffer(wkb_geometry::geography, %s)::geometry, ST_Buffer(wkb_geometry::geography, %s)::geometry)::geography) / 0.3048 ^ 2 sqft, ogc_fid FROM api_streetcenterline WHERE ogc_fid=%s", [street_width_m, sidewalk_walking_width_m, closest_street]):
            return street.sqft

class StreetCenterline(models.Model):
    ogc_fid = models.IntegerField(primary_key=True)
    wkb_geometry = models.MultiLineStringField()
    objectid = models.DecimalField(max_digits=5, decimal_places=0)
    fnode = models.DecimalField(max_digits=5, decimal_places=0)
    tnode = models.DecimalField(max_digits=5, decimal_places=0)
    lpoly = models.CharField(max_length=1)
    rpoly = models.CharField(max_length=1)
    length = models.DecimalField(max_digits=24, decimal_places=15)
    stc12 = models.CharField(max_length=1)
    stcl2_id = models.CharField(max_length=1)
    pre_dir = models.CharField(max_length=2)
    st_name = models.CharField(max_length=28)
    st_type = models.CharField(max_length=4)
    suf_dir = models.CharField(max_length=5)
    zip_left = models.DecimalField(max_digits=5, decimal_places=0)
    zip_right = models.DecimalField(max_digits=5, decimal_places=0)
    l_f_add = models.DecimalField(max_digits=5, decimal_places=0)
    l_t_add = models.DecimalField(max_digits=5, decimal_places=0)
    r_f_add = models.DecimalField(max_digits=5, decimal_places=0)
    r_t_add = models.DecimalField(max_digits=5, decimal_places=0)
    st_code = models.DecimalField(max_digits=5, decimal_places=0)
    l_hundred = models.DecimalField(max_digits=5, decimal_places=0)
    r_hundred = models.DecimalField(max_digits=5, decimal_places=0)
    seg_id = models.DecimalField(max_digits=7, decimal_places=0)
    oneway = models.CharField(max_length=2)
    class_field = models.DecimalField(max_digits=2, decimal_places=0)
    responsibl = models.CharField(max_length=14)
    update = models.DateField()
    newsegdate = models.DateField()
    multi_rep = models.DecimalField(max_digits=1, decimal_places=0)
    streetlabe = models.CharField(max_length=32)
    stname = models.CharField(max_length=32)
    shape_len = models.DecimalField(max_digits=24, decimal_places=15)

    objects = models.Manager()
    closest_sidewalk = SidewalkManager()

    # Returns the string representation of model
    def __str__(self):
        return self.stname
