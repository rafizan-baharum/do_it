import folium

# create map
m = folium.Map(location=[3.1483425, 101.70737], zoom_start=12)


# Global tooltip
tooltip = 'Klik untuk Maklumat Lanjut'

# Create markers
folium.Marker([101.71042,3.06199],
	popup='<strong>PPR RAYA PERMAI</strong>',
	tooltip=tooltip,
	icon=folium.Icon(icon='cloud')).add_to(m)
folium.Marker([3.1643,101.70571],
	popup='<strong>KAMPONG BHARU</strong>',
	tooltip=tooltip,
	icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([3.22003,101.70571],
	popup='<strong>PPR TAMAN WAHYU II</strong>',
	tooltip=tooltip,
	icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([3.12738,101.70838],
	popup='<strong>PPR SERI ALAM</strong>',
	tooltip=tooltip,
	icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([3.13651,101.70545],
	popup='<strong>PA SERI SARAWAK</strong>',
	tooltip=tooltip,
	icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([3.09148,101.70553],
	popup='<strong>PPR SALAK SELATAN</strong>',
	tooltip=tooltip,
	icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([3.16318,101.73279],
	popup='<strong>PPR JELATEK</strong>',
	tooltip=tooltip,
	icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([3.22187,101.72097],
	popup='<strong>PA SERI TIOMAN 1</strong>',
	tooltip=tooltip,
	icon=folium.Icon(icon='cloud')).add_to(m)


# Generate Map
m.save('kl_center_map.html')
