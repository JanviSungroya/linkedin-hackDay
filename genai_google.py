import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def generate_referral_request(job_desc, user_profile, referral_contact,referrer_college):
    llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.2,
    max_tokens=None,
    timeout=None,
  )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a professional networking assistant. Your task is to create a personalized referral request from the job seeking person.
                Analyze the profile of user and extract his strong skills that will be helpful for getting him referral.
                Also Analyze the similarities between user and referrer profile. For example - if both of them have same college , you can mention thisline in response.
                Based on this analysis, craft a compelling and personalized referral request that highlights the user's qualifications and suitability for the job.
                
               Example of REFERRAL REQUEST TEMPLATE - 
                Subject: Referral Request for Software Development Engineer II Position at Microsoft

                    Hi [Senior's Name],

                    I hope this message finds you well. I am Utkarsh Tiwari, a fourth-year student at BITS, currently pursuing my degree in [Your Degree Program]. I am reaching out to seek your support for a referral for the Software Development Engineer II position at Microsoft.
                    
                    With extensive knowledge in web development and a strong foundation in various programming languages, I have honed my skills through numerous AI projects and internships. Below is a summary of my technical skill set:

                    Programming Languages: C++, C#, C, GO, Java, JavaScript, PHP, Python, R, Swift
                    Web Development: Extensive experience with front-end and back-end development, including [mention any specific frameworks or tools]
                    AI Projects: Worked on [briefly mention a few AI projects you are particularly proud of]
                    I am particularly drawn to Microsoft due to its innovative environment and commitment to cutting-edge technology. I believe that my background in software development and my passion for AI would allow me to make meaningful contributions to your team.

                    I would be incredibly grateful if you could refer me for the Software Development Engineer II position. Attached is my resume for your reference. Please let me know if there is any additional information you need from my side.

                    Thank you very much for considering my request. I look forward to hearing from you soon.

                    Best regards,

                    Utkarsh Tiwari
                    [Your LinkedIn Profile]
                    [Your Contact Information]
                    [Attachment: Resume]
                    
                    MAKE SURE THAT THIS IS NOT AN EMAIL TEMPLATE. IT IS A REFERRAL REQUEST TEMPLATE. DO NOT INCLUDE LINE 'I hope this email finds you well.'

                JOB DESCRIPTION:
                {job_desc}

                USER-PROFILE:
                {user_profile}

                REFERRAL CONTACT:
                {referral_contact}
                
                REFERRAL COLLEGE :
                {referrer_college}

                Please write a concise and engaging referral request.""",
            ),
            ("human", "{input}"),
        ]
    )

    chain = prompt | llm
    response  = chain.invoke(
        {
            "job_desc": job_desc,
            "user_profile": user_profile,
            "referral_contact":referral_contact,
            "referrer_college":referrer_college,
            "input": "can you please a very effective and attractive referral template for me on the basis of the job description and my user profile",
        }
    )

    # print(response.content)
    return response.content



# job_desc = """Job Title: Senior Sales Engineer
# Job ID: 123
# Location: Redmond, WA
# Job Description:
# Microsoft is seeking a passionate and talented Senior Sales Engineer to join our dynamic team. In this role, you will have the opportunity to work on cutting-edge technologies, develop innovative solutions, and contribute to the development of software products that empower millions of people around the world.

# Key Responsibilities:
# Design, develop, and maintain software applications and systems.
# Collaborate with cross-functional teams to define, design, and ship new features.
# Write clean, scalable, and efficient code.
# Conduct code reviews and provide constructive feedback to team members.
# Troubleshoot, debug, and optimize software applications.
# Stay up-to-date with the latest industry trends, technologies, and best practices.
# Participate in all phases of the software development lifecycle, including planning, development, testing, and deployment.
# Qualifications:
# Bachelor’s degree in Computer Science, Software Engineering, or a related field.
# Proven experience as a Software Engineer or similar role.
# Proficiency in one or more programming languages such as C#, C++, Java, or Python.
# Strong problem-solving skills and attention to detail.
# Excellent communication and teamwork abilities.
# Experience with software development tools and methodologies.
# Knowledge of cloud computing, machine learning, or AI is a plus.
# Preferred Skills:
# Experience with Microsoft Azure or other cloud platforms.
# Familiarity with agile development methodologies.
# Knowledge of DevOps practices and tools.
# Strong understanding of data structures, algorithms, and software design principles.
# Experience with front-end technologies (e.g., HTML, CSS, JavaScript) and frameworks (e.g., React, Angular).
# Benefits:
# Competitive salary and performance-based bonuses.
# Comprehensive health, dental, and vision insurance.
# 401(k) plan with company match.
# Generous paid time off and holidays.
# Professional development opportunities.
# Employee wellness programs and resources.
# Collaborative and inclusive work environment."""


# user_profile = """
# User Profile: John Doe

# Skills:
# Programming Languages: Proficient in C#, Java, Python, and C++. Experienced with JavaScript, HTML, and CSS.
# Frameworks & Libraries: Expertise in .NET, React, Angular, and Node.js.
# Cloud Platforms: Skilled in Microsoft Azure, AWS, and Google Cloud Platform.
# Databases: Experienced with SQL Server, MySQL, and NoSQL databases like MongoDB.
# Tools & Technologies: Proficient with Git, Docker, Kubernetes, Jenkins, and Visual Studio.
# Software Development Methodologies: Strong understanding of Agile, Scrum, and DevOps practices.
# Machine Learning & AI: Knowledgeable in machine learning algorithms, neural networks, and AI applications.
# Projects:
# Project Name: E-commerce Platform

# Description: Developed a scalable e-commerce platform using .NET and React. Implemented features such as user authentication, product catalog management, shopping cart, and payment gateway integration.
# Technologies Used: C#, .NET, React, SQL Server, Azure.
# Project Name: Cloud-Based Inventory Management System

# Description: Designed and developed a cloud-based inventory management system for a retail client. The system included real-time inventory tracking, order management, and reporting features.
# Technologies Used: Java, Spring Boot, Angular, MySQL, AWS.
# Project Name: AI-Powered Chatbot

# Description: Created an AI-powered chatbot for customer service using natural language processing and machine learning techniques. The chatbot was integrated into the client’s website and mobile app to provide 24/7 customer support.
# Technologies Used: Python, TensorFlow, Flask, JavaScript, Google Cloud Platform.
# Project Name: DevOps Automation

# Description: Led a project to automate the CI/CD pipeline for a large-scale application. Implemented automated testing, continuous integration, and continuous deployment using Jenkins, Docker, and Kubernetes.
# Technologies Used: Jenkins, Docker, Kubernetes, Git, Azure DevOps.
# Project Name: Real-Time Analytics Dashboard

# Description: Developed a real-time analytics dashboard for monitoring application performance and user engagement. The dashboard provided visualizations and insights using data from multiple sources.
# Technologies Used: Node.js, Express, D3.js, MongoDB, AWS.
# Professional Summary:
# John Doe is a highly skilled and motivated Software Engineer with over 5 years of experience in developing, deploying, and maintaining software applications. He has a strong background in various programming languages, frameworks, and cloud platforms. John is passionate about leveraging cutting-edge technologies to create innovative solutions that meet business needs. He is a team player with excellent problem-solving skills and a commitment to continuous learning and improvement.
# """

# referral_contact="Mr. John Dee"

# # referral_request = generate_referral_request(job_desc, user_profile, referral_contact)
# # # print(referral_request)
# # return referral_request

