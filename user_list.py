import uuid

users_data = [
    {
        "email": "olasmith@gmail.com",
        "first_name": "Ola",
        "last_name": "Smith",
        "about": "A web developer passionate about building responsive web apps",
        "tags": ['Web Development', 'CSS', 'Javascript', 'HTML'],
        "picture_uri": "collabio/profile_picture",
        "user_id":  str(uuid.uuid4()),
    },
    {
        "email": "alimatsadiat@gmail.com",
        "first_name": "Alimat",
        "last_name": "Sadiat",
        "about": "An android developer passionate about building intuitive mobile apps",
        "tags": ['Android', 'Kotlin', 'Java'],
        "picture_uri": "collabio/profile_picture",
        "user_id":  str(uuid.uuid4()),
    }
]
users_data.extend([
    {
        "email": "jamescook@example.com",
        "first_name": "James",
        "last_name": "Cook",
        "about": "A passionate web developer and food enthusiast",
        "tags": ['Web Development', 'Food', 'Cooking'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "alexandra@example.com",
        "first_name": "Alexandra",
        "last_name": "Johnson",
        "about": "A mobile app developer with a love for travel",
        "tags": ['Mobile App Development', 'Travel', 'iOS', 'Android'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "david@example.com",
        "first_name": "David",
        "last_name": "Mitchell",
        "about": "A graphic designer passionate about creating visual identities",
        "tags": ['Graphic Design', 'Brand Identity', 'Logo Design'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "maria@example.com",
        "first_name": "Maria",
        "last_name": "Rodriguez",
        "about": "A language enthusiast and app developer",
        "tags": ['Language Learning', 'Mobile App Development', 'iOS', 'Android'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "sophia@example.com",
        "first_name": "Sophia",
        "last_name": "Turner",
        "about": "An artist in search of a digital canvas",
        "tags": ['Art', 'Web Development', 'Portfolio Website'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "adekunlelawal@example.com",
        "first_name": "Adekunle",
        "last_name": "Lawal",
        "about": "A sustainable fashion expert committed to eco-friendly design",
        "tags": ['Fashion Design', 'Sustainable Fashion', 'Ethical Production'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "stellaadeniyi@example.com",
        "first_name": "Stella",
        "last_name": "Adeniyi",
        "about": "A game development enthusiast specializing in virtual reality",
        "tags": ['Game Development', 'Virtual Reality', 'VR', 'Gaming'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "chibuikeezeiru@example.com",
        "first_name": "Chibuike",
        "last_name": "Ezeiru",
        "about": "A developer dedicated to providing accurate weather data",
        "tags": ['Mobile App Development', 'Weather', 'iOS', 'Android'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "yemiowoeye@example.com",
        "first_name": "Yemi",
        "last_name": "Owoeye",
        "about": "A graphic designer with innovative ideas",
        "tags": ['Graphic Design', 'Logo Design', 'Brand Identity'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "yemisicoker@example.com",
        "first_name": "Yemisi",
        "last_name": "Coker",
        "about": "A web developer interested in building a digital platform for discussion",
        "tags": ['Web Development', 'Blogging', 'Content Management'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "godwinsmart@example.com",
        "first_name": "Godwin",
        "last_name": "Smart",
        "about": "A blockchain enthusiast creating a cryptocurrency exchange",
        "tags": ['Blockchain Development', 'Cryptocurrency', 'Exchange'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "opeyemiadetutu@example.com",
        "first_name": "Opeyemi",
        "last_name": "Adetutu",
        "about": "A web developer and art lover in search of an online showcase",
        "tags": ['Web Development', 'Art Gallery', 'Virtual Gallery'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "michaeljones@example.com",
        "first_name": "Michael",
        "last_name": "Jones",
        "about": "A mobile app developer promoting sustainable and eco-friendly agriculture",
        "tags": ['Mobile App Development', 'Agriculture', 'Sustainability', 'iOS', 'Android'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "liliansalami@example.com",
        "first_name": "Lilian",
        "last_name": "Salami",
        "about": "An educator and web designer revolutionizing online learning",
        "tags": ['Web Design', 'E-learning', 'Education'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "ososine@example.com",
        "first_name": "Osos",
        "last_name": "Inegbedion",
        "about": "A mobile app developer and adventurer creating a travel booking app",
        "tags": ['Mobile App Development', 'Travel', 'iOS', 'Android'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "adedejiolorunwa@example.com",
        "first_name": "Adedeji",
        "last_name": "Olorunwa",
        "about": "Tech enthusiast making homes smarter",
        "tags": ['IoT', 'Smart Home', 'Automation'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
    {
        "email": "ianclark@example.com",
        "first_name": "Ian",
        "last_name": "Clark",
        "about": "Meditation and mindfulness enthusiast creating a calming app",
        "tags": ['Mobile App Development', 'Meditation', 'Mindfulness', 'iOS', 'Android'],
        "picture_uri": "collabio/profile_picture",
        "user_id": str(uuid.uuid4())
    },
{
    "email": "georgeemmanuel@example.com",
    "first_name": "George",
    "last_name": "Emmanuel",
    "about": "Educator pioneering virtual reality learning experiences",
    "tags": ['VR Development', 'Education', 'Virtual Reality'],
    "picture_uri": "collabio/profile_picture",
    "user_id": str(uuid.uuid4())
},
{
    "email": "hopelove@example.com",
    "first_name": "Hope",
    "last_name": "Love",
    "about": "A graphic designer working towards positive change",
    "tags": ['Graphic Design', 'Logo Design', 'Non-Profit'],
    "picture_uri": "collabio/profile_picture",
    "user_id": str(uuid.uuid4())
},
{
    "email": "victormonday@example.com",
    "first_name": "Victor",
    "last_name": "Monday",
    "about": "Web developer and community builder focused on creating a platform for discussions",
    "tags": ['Web Development', 'Community Forum', 'Discussion'],
    "picture_uri": "collabio/profile_picture",
    "user_id": str(uuid.uuid4())
},
{
    "email": "modupelawal@example.com",
    "first_name": "Modupe",
    "last_name": "Lawal",
    "about": "Marketplace enthusiast connecting 3D printing services and designers",
    "tags": ['3D Printing', 'Marketplace', 'Technology'],
    "picture_uri": "collabio/profile_picture",
    "user_id": str(uuid.uuid4())
},
{
    "email": "markboston@example.com",
    "first_name": "Mark",
    "last_name": "Boston",
    "about": "Language enthusiast connecting people through translation",
    "tags": ['Mobile App Development', 'Translation', 'Language', 'iOS', 'Android'],
    "picture_uri": "collabio/profile_picture",
    "user_id": str(uuid.uuid4())
},
{
    "email": "hildaezekafor@example.com",
    "first_name": "Hilda",
    "last_name": "Ezekafor",
    "about": "Fitness enthusiast promoting a healthy lifestyle",
    "tags": ['Mobile App Development', 'Fitness', 'Nutrition', 'iOS', 'Android'],
    "picture_uri": "collabio/profile_picture",
    "user_id": str(uuid.uuid4())
}, 
])
