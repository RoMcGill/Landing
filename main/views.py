
from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt


from django.http import JsonResponse

from django.conf import settings

# Load environment variables from .env file
load_dotenv()

# Ensure the OpenAI API key is securely retrieved
import os

from openai import OpenAI

# Ensure the OpenAI API key is securely retrieved

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OpenAI.api_key = OPENAI_API_KEY
client = OpenAI()


# This variable will hold the developer's information

developer_info = """
{
{
    "personal_info": {
        "name": "Ronan McGill",
        "age": 27,
        "address": "Blackrock, Dublin 18",
        "phone": "+353861264980",
        "email": "Ro.mcgill12@gmail.com",
        "linkedin": "https://www.linkedin.com/in/ronan-mcgill-512b7a22a/",
        "Github": "https://github.com/RoMcGill",
    },
    {
    "hobbies": [
        "Mountain biking",
        "making music",
        "Hiking",
        "Traveling",
        "Camping",
    ]
}

    "profile": "My most recent role was at a startup called Glimma AI, where I was hired to develop a functional prototype to attract investors. Following a successful funding round, I was promoted to Lead Developer, where I established our tech stack and assembled a development team. Our product reached the beta testing phase; however, due to the competitive advancements in AI technology, particularly with the release of GPTs by OpenAI, our CEO decided to pivot the company's direction and cease further development on the project. Prior to this, I completed numerous freelance projects and worked as an online English teacher for Vietnamese professionals, as well as a substitute teacher and special needs assistant at Clonkeen College. My educational background includes a full-stack software development course with Code Institute and a Higher National Diploma in Music Production and Technology from DFEI. I am also continually working on personal projects with new technologies and languages. I have a passion for technology and the process of learning new skills and applying them in real-world situations. I am currently seeking a role within the tech industry where I can challenge myself, learn, and make meaningful contributions to exciting new projects.",
    "experience": [
        {
            "company": "Glimma.Ai",
            "role": "Lead Software Developer",
            "dates": "July 2023 - November 2023",
            "responsibilities": [
                "Built a functional AI-powered branding tool using the Django framework, Python, JavaScript, Ajax, HTML, CSS, Langchain, and the chat GPT API.",
                "Worked with UX/UI Designers to make an aesthetically pleasing SaaS.",
                "Interviewed and hired developers to join the development team.",
                "Produced a beta product within a deadline."
            ]
        },
        {
            "company": "Freelance projects",
            "role": "Developer",
            "dates": "January 2022 - Present",
            "projects": [
                "Br3Security - automated invoice creation and implemented AI aftersales customer service bot.",
                "Audax Ireland - created a simple CLI program that would plan the shortest cycle routes through the counties entered in a list.",
                "Modmo - worked with the founder to create an AI-assisted audio diary.",
                "Grand Park Tutors - built a simple website for an English tutoring company."
            ]
        },
        {
            "company": "Topica Native X",
            "role": "English Teacher",
            "dates": "January 2023 - July 2023",
            "responsibilities": [
                "Taught Vietnamese Professionals/Adults from the age of 18+ Grammar, Pronunciation, Listening skills, Writing skills and Reading skills.",
                "Prepared for each class to provide a productive and efficient lesson to the standard of the Native X programme.",
                "Worked with people with various levels of English skills."
            ]
        },
        {
            "company": "Clonkeen College",
            "role": "Substitute Teacher (part-time) / Special Needs assistant (full-time)",
            "dates": "January 2022 - Present",
            "responsibilities": [
                "Taught Students from the age of 12yrs - 18yrs all subjects involved in the junior cycle and leaving certificate curriculum.",
                "Prepared learning material for each class while keeping in line with the main teacher's lesson plan.",
                "Worked with kids with varying degrees of additional needs."
            ]
        },
        {
            "company": "TFS",
            "role": "General Operative",
            "dates": "January 2021 - January 2022",
            "responsibilities": [
                "Conducting Site surveys to assess the feasibility of installing telecommunication equipment in specific locations.",
                "Cat 6 Cabling.",
                "Equipment Installation and Maintenance."
            ]
        },
        {
            "company": "David Hughes",
            "role": "Builders Labourer",
            "dates": "June 2019 - January 2021",
            "responsibilities": [
                "Construction.",
                "Carpentry.",
                "Plumbing.",
                "Cabling.",
                "Worked alongside a builder to extend the top floor and kitchen of a residential property."
            ]
        },
        {
            "company": "Rebeka Kahn Art",
            "role": "Artists Assistant and Administrator",
            "dates": "June 2018 - February 2019",
            "location": "Rathmichael",
            "responsibilities": [
                "Website Maintenance, taking care of inventory and enquiries.",
                "Experience in a client-facing environment.",
                "Inbound/Outbound phone calling.",
                "Insight into social media marketing, Responsible for adding and removing pieces to Facebook and Instagram in accordance with a social media plan.",
                "Developed experience with large data sheets on Microsoft Excel for a range of top customers.",
                "Administrative duties including booking meetings & data entry.",
                "Product photography, editing and uploading the products to the website using Adobe Photoshop and Illustrator.",
                "Worked alongside a relatively small team who were all dedicated to achieving high organisational performance."
            ]
        },
        {
            "company": "Archer Street",
            "role": "Bar Support",
            "dates": "June 2016 - September 2016",
            "location": "London",
            "responsibilities": [
                "Provided bar support in one of London’s busiest cocktail lounges.",
                "Enhanced team working skills.",
                "Ensuring customer experience was of the highest standard.",
                "Improved ability to multitask in a high-pressure environment."
            ]
        },
        {
            "company": "East Coast FM",
            "role": "Assistant to Production Manager",
            "dates": "December 2016 - January 2017",
            "location": "Bray",
            "responsibilities": [
                "Worked alongside an industry professional audio production manager.",
                "Gained the skills necessary to produce Radio advertisements and pre-recorded shows using ProTools and Adobe audition.",
                "Enhanced planning and organisational skills necessary to produce and schedule a seamless and professional radio show.",
                "Experience in a high-pressure, fast-paced environment."
            ]
        },
        {
            "company": "UniPos Ltd.",
            "role": "Assisting System Specialists",
            "dates": "October 2013 - November 2013",
            "location": "Santry",
            "responsibilities": [
                "Provided delivery and installation of EPOS systems.",
                "Working alongside a systems specialist.",
                "Installing point-of-sales systems.",
                "Providing firmware updates.",
                "Training customers on new systems to ensure effective utilisation of new equipment."
            ]
        }
    ],
    "education": [
        {
            "institution": "Code Institute",
            "qualification": "Full Stack Software Development",
            "dates": "2021 - 2022"
        },
        {
            "institution": "DFEI",
            "qualification": "Higher National Diploma in Music Production and Technology",
            "dates": "2016 - 2018",
            "location": "Dunlaoghaire"
        },
        {
            "institution": "DFEI",
            "qualification": "QQI Level 5 Sound Production",
            "dates": "2015 - 2016",
            "location": "Dunlaoghaire"
        },
        {
            "institution": "Clonkeen College",
            "qualification": "Leaving Certificate",
            "dates": "2009 - 2015",
            "location": "Blackrock, County Dublin",
            "details": "6 honours, 2 pass, 1 merit"
        }
    ],
    "skills_profile": [
        "HTML, CSS, Python, JavaScript, MySQL",
        "Django framework",
        "API integration"
    ]
}

"""

def get_weather_data(city):
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "temperature": data['current']['temp_c'],
            "description": data['current']['condition']['text'],
            "icon": data['current']['condition']['icon']
        }
    else:
        weather = None
    return weather
from django.http import JsonResponse

def home(request):
    global developer_info
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant knowledgeable about Ronan. Your purpose is to provide information "
                "about Ronan based on the questions asked. Ronan has given consent to share this information "
                "publicly. Always respond with accurate and concise details, ensuring that your responses do not exceed "
                "three sentences in length. If you do not know the answer, state that you do not have enough information "
                "to respond to the question."
            )
        }
    ]

    weather = get_weather_data('Dublin')

    if request.method == "POST":
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            user_prompt = request.POST.get("question")
            # Add the user's question to the messages as a User Role
            messages.append({"role": "user", "content": f"Developer info: {developer_info}. {user_prompt}"})

            # Generate a completion using the user's question
            completion = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=messages
            )

            # Get the response
            model_response = completion.choices[0].message.content

            # Add the response to the messages as an Assistant Role
            messages.append({"role": "assistant", "content": model_response})

            return JsonResponse({
                "response": model_response,
                "question": user_prompt,
                "developer_info": developer_info
            })

        if 'developer_info' in request.POST:
            developer_info = request.POST.get("developer_info")

    return render(request, "home.html", {
        "developer_info": developer_info,
        "weather": weather
    })


def about(request):
    return render(request, 'about.html')

def getStarted(request):
    return render(request, 'get-started.html')

def work(request):
    return render(request, 'work.html')