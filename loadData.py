import os
os.environ['DJANGO_SETTINGS_MODULE']='backend.settings'

import sys
sys.path.append('/home/rmehta/astrosat/backend')

import django
django.setup()

from astrosat.models import CosmicSource

f = open('lmxbcat.dat', 'r')

i = 0
while True:
    i += 1
    line = f.readline()
    if not line: break

    name = line[:16]

    rah = int(line[24:26])
    ram = int(line[27:29])
    ras = float(line[30:36])

    equatorial_ra = ((rah-12.) + (ram/60.) + (ras/3600.))*15

    dec_sign = line[37]
    dec_d = int(line[38: 40])
    dec_m = int(line[41:43])
    dec_s = float(line[44:49]) if (line[44:49].isspace() == False) else 0.

    equatorial_dec = (-1 if dec_sign == "-" else 1)*(dec_d + dec_m/60. + dec_s/3600.)

    galactic_longitude = float(line[51:57])

    galactic_latitude = float(line[58:66])

    type_of_observation = line[17:23]

    positional_accuracy = float(line[72:79]) if (line[72:79].isspace() == False) else None
    
    optical_counterpart_name = line[80:97]

    v_magnitude = float(line[116:122]) if (line[116:122].isspace() == False) else None

    b_v_color_index = float(line[130:136]) if (line[130:136].isspace() == False) else None

    u_b_color_index = float(line[143:148]) if (line[143:148].isspace() == False) else None

    spectral_type = line[316:328]

    x_ray_flux = float(line[185:196]) if (line[185:196].isspace() == False) else None

    orbital_period = float(line[242:252]) if (line[242:252].isspace() == False) else None

    pulse_period = float(line[259:270]) if (line[259:270].isspace() == False) else None

    name2 = line[329:342]

    name3 = line[344:359]

    print(i)
    source = CosmicSource(
        name = name, 
        equatorial_ra = equatorial_ra, 
        equatorial_dec = equatorial_dec, 
        galactic_longitude = galactic_longitude, 
        galactic_latitude = galactic_latitude, 
        type_of_observation = type_of_observation,
        positional_accuracy = positional_accuracy,
        optical_counterpart_name = optical_counterpart_name,
        v_magnitude = v_magnitude,
        b_v_color_index = b_v_color_index,
        u_b_color_index = u_b_color_index,
        spectral_type = spectral_type,
        x_ray_flux = x_ray_flux,
        orbital_period = orbital_period,
        pulse_period = pulse_period,
        name2 = name2,
        name3 = name3
    )

    # print(equatorial_ra, i)


    source.save()


    
    

