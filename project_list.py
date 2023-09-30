from datetime import datetime, timedelta
import uuid

# Generate timestamp and interval
now = datetime.now()
interval = timedelta(minutes=60)

projects_data = [
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Build an e-commerce website',
        'timestamp': (now - interval * 1).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I am looking for a web developer to collaborate with me to build an e-commerce website using Shopify or WooCommerce.

The website will have a modern and responsive design.

It will include features such as product listings, shopping cart, and secure payment integration.

The project will consist of building the user interface, developing the front-end and back-end functionality, integrating the website with a payment gateway, testing the website and ensuring a smooth user experience.

The target audience for the website is customers who want to purchase products online.

If you are interested in collaborating with me, please send me a message.
        ''',
        'tags': ['Web Development', 'E-commerce', 'Shopify', 'WooCommerce'],
        'poster_name': 'Ola Smith',
        'poster_email': 'olasmith@gmail.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Develop a mobile app for a fitness tracker',
        'timestamp': (now - interval * 2).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I am looking for a mobile app developer to collaborate with me to create a fitness tracker app for iOS and Android.

The app would allow users to track their daily activities, set fitness goals, and monitor their progress.

The project will consist of building the app's user interface, implementing the tracking and goal-setting functionality, integrating the app with health data APIs, testing the app and ensuring a seamless user experience.

The target audience for the app is fitness enthusiasts who want to monitor their physical activities and stay motivated.

If you are interested in collaborating with me on this project, please send me a message.
        ''',
        'tags': ['Mobile App Development', 'Fitness', 'iOS', 'Android'],
        'poster_name': 'Alimat Sadiat',
        'poster_email': 'alimatsadiat@gmail.com'
    }
]


projects_data.extend([
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Create a Recipe Sharing Website',
        'timestamp': (now - interval * 4).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm seeking a web developer to partner with me in building a recipe sharing website. The site should enable users to post, search for, and rate recipes.

We want an intuitive user interface, user-friendly recipe submission forms, and a robust search feature. Additionally, it should allow users to rate and comment on recipes.

If you're enthusiastic about cooking and web development, reach out to me!
        ''',
        'tags': ['Web Development', 'Recipe Sharing', 'Food', 'Community'],
        'poster_name': 'James Cook',
        'poster_email': 'jamescook@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Build a Social Networking App',
        'timestamp': (now - interval * 5).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm looking for a skilled mobile app developer to help create a social networking app. This app should allow users to connect, share updates, and message each other.

We need a user-friendly interface, secure messaging features, and the ability to post photos and videos. Let's build the next big social platform together!

Interested? Get in touch!
        ''',
        'tags': ['Mobile App Development', 'Social Networking', 'iOS', 'Android'],
        'poster_name': 'Alexandra Johnson',
        'poster_email': 'alexandra@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Design a Business Logo',
        'timestamp': (now - interval * 6).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm seeking a up and coming graphic designer to partner with me in creating a unique and eye-catching logo for a startup business. The logo would reflect the essence of the brand and resonate with the target audience.

If you have a passion for design and branding, please reach out!
        ''',
        'tags': ['Graphic Design', 'Logo Design', 'Brand Identity'],
        'poster_name': 'David Mitchell',
        'poster_email': 'david@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Develop a Language Learning App',
        'timestamp': (now - interval * 7).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm in search of a mobile app developer to collaborate on a language learning app. This app should help users learn new languages through interactive lessons, quizzes, and speech recognition.

We aim for an engaging user experience and the ability to learn multiple languages. Join me in making language learning accessible to all!
        ''',
        'tags': ['Mobile App Development', 'Language Learning', 'Education', 'iOS', 'Android'],
        'poster_name': 'Maria Rodriguez',
        'poster_email': 'maria@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Build a Portfolio Website for an Artist',
        'timestamp': (now - interval * 8).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm looking for a web developer to partner with me in creating a stunning portfolio website for my art. The website should showcase my artwork beautifully and have an easy-to-navigate gallery.

If you have a passion for art and web development, let's collaborate on this artistic project!
        ''',
        'tags': ['Web Development', 'Portfolio Website', 'Art', 'Gallery'],
        'poster_name': 'Sophia Turner',
        'poster_email': 'sophia@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Design a Sustainable Fashion Line Website',
        'timestamp': (now - interval * 9).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm searching for a web designer to help me design a sustainable fashion line website. We are committed to eco-friendly materials and ethical production.

If you're passionate about sustainable fashion and have web design skills, let's create a positive impact on the fashion industry!
        ''',
        'tags': ['Web Design', 'Sustainable Fashion', 'Ethical Production'],
        'poster_name': 'Adekunle Lawal',
        'poster_email': 'adekunlelawal@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Develop a Virtual Reality Game',
        'timestamp': (now - interval * 10).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm seeking a game developer to collaborate with me on an exciting virtual reality (VR) game project. The game should offer immersive experiences and interactive gameplay.

If you're passionate about VR and game development, let's dive into this exciting venture!
        ''',
        'tags': ['Game Development', 'Virtual Reality', 'VR', 'Gaming'],
        'poster_name': 'Stella Adeniyi',
        'poster_email': 'stellaadeniyi@example.com'
    }
])


projects_data.extend([
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Develop a Weather App',
        'timestamp': (now - interval * 11).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm looking for a mobile app developer to collaborate on a weather app project. The app should provide real-time weather information, forecasts, and alerts for users' locations.

We aim for accurate data and an intuitive user interface. Join me in creating a useful weather app!
        ''',
        'tags': ['Mobile App Development', 'Weather', 'iOS', 'Android'],
        'poster_name': 'Chibuike Ezeiru',
        'poster_email': 'chibuikeezeiru@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Design a Brand Logo for a Startup',
        'timestamp': (now - interval * 12).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm seeking a graphic designer to collaborate with me to create a memorable brand logo for a startup. The logo would capture the essence of the brand and resonate with the target audience.

If you're passionate about branding and design, let's make our mark in the market!
        ''',
        'tags': ['Graphic Design', 'Logo Design', 'Brand Identity'],
        'poster_name': 'Yemi Owoeye',
        'poster_email': 'yemiowoeye@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Build a Blogging Platform',
        'timestamp': (now - interval * 13).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm in search of a web developer to collaborate on building a blogging platform. The platform should allow users to create, edit, and publish blog posts with ease.

We aim for a user-friendly interface and robust content management features. Join me in creating a platform for bloggers!
        ''',
        'tags': ['Web Development', 'Blogging', 'Content Management'],
        'poster_name': 'Yemisi Coker',
        'poster_email': 'yemisicoker@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Develop a Cryptocurrency Exchange',
        'timestamp': (now - interval * 14).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm looking for a blockchain developer to collaborate on a cryptocurrency exchange project. The exchange should offer secure trading, wallet integration, and real-time market data.

If you're passionate about blockchain technology and cryptocurrencies, let's build a cutting-edge exchange!
        ''',
        'tags': ['Blockchain Development', 'Cryptocurrency', 'Exchange'],
        'poster_name': 'Godwin Smart',
        'poster_email': 'godwinsmart@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Create a Virtual Art Gallery',
        'timestamp': (now - interval * 15).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm seeking a web developer to collaborate with me in creating a virtual art gallery to showcase artworks. The gallery would provide an immersive experience for art enthusiasts.

We aim to replicate the feel of a physical gallery online. Join me in showcasing art in a unique way!
        ''',
        'tags': ['Web Development', 'Art Gallery', 'Virtual Gallery'],
        'poster_name': 'Opeyemi Adetutu',
        'poster_email': 'opeyemiadetutu@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Build a Sustainable Agriculture App',
        'timestamp': (now - interval * 16).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm looking for a mobile app developer to collaborate on an app for sustainable agriculture. The app would provide resources, tips, and tools for eco-friendly farming practices.

If you're passionate about agriculture and sustainability, let's cultivate a greener future!
        ''',
        'tags': ['Mobile App Development', 'Agriculture', 'Sustainability', 'iOS', 'Android'],
        'poster_name': 'Michael Jones',
        'poster_email': 'michaeljones@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Design an E-learning Platform',
        'timestamp': (now - interval * 17).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm seeking a web designer to collaborate on an e-learning platform project. The platform would offer a seamless learning experience with interactive courses and assessments.

If you're passionate about education and web design, let's empower learners together!
        ''',
        'tags': ['Web Design', 'E-learning', 'Education'],
        'poster_name': 'Lilian Salami',
        'poster_email': 'liliansalami@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Develop a Travel Booking App',
        'timestamp': (now - interval * 18).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm looking for a mobile app developer to collaborate on a travel booking app. The app should allow users to book flights, hotels, and activities seamlessly.

If you're passionate about travel and mobile app development, let's explore the world together!
        ''',
        'tags': ['Mobile App Development', 'Travel', 'iOS', 'Android'],
        'poster_name': 'Osos Inegbedion',
        'poster_email': 'ososine@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Build a Smart Home Automation System',
        'timestamp': (now - interval * 19).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm in search of a developer to collaborate on a smart home automation project. The system would enable users to control and monitor their home appliances remotely.

If you're excited about IoT and home automation, let's make homes smarter!
        ''',
        'tags': ['IoT', 'Smart Home', 'Automation'],
        'poster_name': 'Adedeji Olorunwa',
        'poster_email': 'adedejiolorunwa@example.com'
    }
])


projects_data.extend([
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Develop a Meditation and Mindfulness App',
        'timestamp': (now - interval * 20).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm seeking a mobile app developer to collaborate on a meditation and mindfulness app. The app should offer guided meditation sessions, stress relief techniques, and daily mindfulness practices.

If you're passionate about mental health and mobile app development, let's help people find inner peace!
        ''',
        'tags': ['Mobile App Development', 'Meditation', 'Mindfulness', 'iOS', 'Android'],
        'poster_name': 'Ian Clark',
        'poster_email': 'ianclark@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Build a Virtual Reality Education Platform',
        'timestamp': (now - interval * 21).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm looking for a developer to collaborate on a virtual reality education platform. The platform should offer immersive learning experiences across various subjects.

If you're passionate about VR and education, let's transform how we learn!
        ''',
        'tags': ['VR Development', 'Education', 'Virtual Reality'],
        'poster_name': 'George Emmanuel',
        'poster_email': 'georgeemmanuel@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Design a Logo for a Non-Profit Organization',
        'timestamp': (now - interval * 22).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm seeking a graphic designer to collaborate on creating a meaningful logo for a non-profit organization. The logo should convey its mission and values.

If you're passionate about using design for a good cause, let's make a difference together!
        ''',
        'tags': ['Graphic Design', 'Logo Design', 'Non-Profit'],
        'poster_name': 'Hope Love',
        'poster_email': 'hopelove@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Develop a Community Forum Website',
        'timestamp': (now - interval * 23).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm in search of a web developer to collaborate with me on creating a community forum website. The platform should enable users to discuss various topics, share ideas, and build a community.

If you're passionate about online communities and web development, let's create a space for meaningful discussions!
        ''',
        'tags': ['Web Development', 'Community Forum', 'Discussion'],
        'poster_name': 'Victor Monday',
        'poster_email': 'victormonday@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Build a 3D Printing Marketplace',
        'timestamp': (now - interval * 24).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm looking for a developer to collaborate on a 3D printing marketplace. The platform should connect users with 3D printing services and designers.

If you're passionate about 3D printing and marketplace development, let's bring creativity to life!
        ''',
        'tags': ['3D Printing', 'Marketplace', 'Technology'],
        'poster_name': 'Modupe Lawal',
        'poster_email': 'modupelawal@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Develop a Language Translation App',
        'timestamp': (now - interval * 25).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm looking for a mobile app developer to collaborate on a language translation app. The app should provide real-time translation for multiple languages.

If you're passionate about breaking language barriers, let's connect the world through communication!
        ''',
        'tags': ['Mobile App Development', 'Translation', 'Language', 'iOS', 'Android'],
        'poster_name': 'Mark Boston',
        'poster_email': 'markboston@example.com'
    },
    {
        'project_id' : str(uuid.uuid4()),
        'title': 'Build a Fitness and Nutrition App',
        'timestamp': (now - interval * 26).strftime('%Y-%m-%d %H:%M:%S'),
        'description': '''I'm in search of a mobile app developer to collaborate on a fitness and nutrition app. The app should provide workout routines, meal plans, and progress tracking.

If you're passionate about health and fitness, let's help people achieve their wellness goals!
        ''',
        'tags': ['Mobile App Development', 'Fitness', 'Nutrition', 'iOS', 'Android'],
        'poster_name': 'Hilda Ezekafor',
        'poster_email': 'hildaezekafor@example.com'
    },
])
