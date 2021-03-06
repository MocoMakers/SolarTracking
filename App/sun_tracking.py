from astropy.coordinates import EarthLocation, AltAz, SkyCoord, get_sun
from astropy.time import Time
import astropy.units as u
from sunpy.coordinates import frames, get_sunearth_distance

def get_azimuth(obstime, latitude, longitude, current_height):
	# We use `~astropy.coordinates.SkyCoord` to define the center of the Sun
	#c = SkyCoord(0 * u.arcsec, 0 * u.arcsec, obstime=obstime, frame=frames.Helioprojective)
	
	c = get_sun(Time(obstime))

	######################################################################################
	# Now we establish our location on the Earth
	# We use the balloon's observational altitude as 'height'. Accuracy of 'height' is
	# far less of a concern than Lon/Lat accuracy.
	current_location = EarthLocation(lon=longitude*u.deg, lat=latitude*u.deg, height=current_height*u.m)


	######################################################################################
	# Now lets convert this to a local measurement of Altitude and Azimuth.

	frame_altaz = AltAz(obstime=Time(obstime), location=current_location)
	sun_altaz = c.transform_to(frame_altaz)
	#print(str(sun_altaz.T))
	return '{0}'.format(sun_altaz.T.alt),'{0}'.format(sun_altaz.T.az)
