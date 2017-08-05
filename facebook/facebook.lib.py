import facebook
import configuration
 

graph = facebook.GraphAPI(access_token=configuration.ACCESS_TOKEN, version='2.9')

page = graph.get_object(id='DonJuanMusicEc', fields='id,artists_we_like,hometown,influences,press_contact,record_label,band_interests,band_members,bio,emails,about,genre,current_location,contact_address,general_manager,booking_agent,birthday,awards,phone,username,website,release_date,is_verified,name,impressum,description')

print(page)

 