from flask import Flask,url_for,redirect,request,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import genai_google
'''
note-> if u want values from html->backend python => have to give values in the url paramter or variable rules
if have to send values from backend to html => then pass variable/value in render_template
'''
college_name= "NIT KKr"
app = Flask(__name__)
job_desc = """Job Title: Software Engineer
    Job ID: 123
    Location: Redmond, WA
    Job Description:
    Microsoft is seeking a passionate and talented Software Engineer to join our dynamic team. In this role, you will have the opportunity to work on cutting-edge technologies, develop innovative solutions, and contribute to the development of software products that empower millions of people around the world.

    Key Responsibilities:
    Design, develop, and maintain software applications and systems.
    Collaborate with cross-functional teams to define, design, and ship new features.
    Write clean, scalable, and efficient code.
    Conduct code reviews and provide constructive feedback to team members.
    Troubleshoot, debug, and optimize software applications.
    Stay up-to-date with the latest industry trends, technologies, and best practices.
    Participate in all phases of the software development lifecycle, including planning, development, testing, and deployment.
    Qualifications:
    Bachelor’s degree in Computer Science, Software Engineering, or a related field.
    Proven experience as a Software Engineer or similar role.
    Proficiency in one or more programming languages such as C#, C++, Java, or Python.
    Strong problem-solving skills and attention to detail.
    Excellent communication and teamwork abilities.
    Experience with software development tools and methodologies.
    Knowledge of cloud computing, machine learning, or AI is a plus.
    Preferred Skills:
    Experience with Microsoft Azure or other cloud platforms.
    Familiarity with agile development methodologies.
    Knowledge of DevOps practices and tools.
    Strong understanding of data structures, algorithms, and software design principles.
    Experience with front-end technologies (e.g., HTML, CSS, JavaScript) and frameworks (e.g., React, Angular).
    Benefits:
    Competitive salary and performance-based bonuses.
    Comprehensive health, dental, and vision insurance.
    401(k) plan with company match.
    Generous paid time off and holidays.
    Professional development opportunities.
    Employee wellness programs and resources.
    Collaborative and inclusive work environment."""
user_profile = f"""
    User Profile: Janvi Sungroya
    College:{college_name}
    Linkedin Profile: "https://www.linkedin.com/in/janvi-sungroya-1b5408234/"
    Email - janvisungroya98@gmail.com
    Contact - 8168212957
    Skills:
    Programming Languages: Proficient in C#, Java, Python, and C++. Experienced with JavaScript, HTML, and CSS.
    Frameworks & Libraries: Expertise in .NET, React, Angular, and Node.js.
    Cloud Platforms: Skilled in Microsoft Azure, AWS, and Google Cloud Platform.
    Databases: Experienced with SQL Server, MySQL, and NoSQL databases like MongoDB.
    Tools & Technologies: Proficient with Git, Docker, Kubernetes, Jenkins, and Visual Studio.
    Software Development Methodologies: Strong understanding of Agile, Scrum, and DevOps practices.
    Machine Learning & AI: Knowledgeable in machine learning algorithms, neural networks, and AI applications.
    Projects:
    Project Name: E-commerce Platform

    Description: Developed a scalable e-commerce platform using .NET and React. Implemented features such as user authentication, product catalog management, shopping cart, and payment gateway integration.
    Technologies Used: C#, .NET, React, SQL Server, Azure.
    Project Name: Cloud-Based Inventory Management System

    Description: Designed and developed a cloud-based inventory management system for a retail client. The system included real-time inventory tracking, order management, and reporting features.
    Technologies Used: Java, Spring Boot, Angular, MySQL, AWS.
    Project Name: AI-Powered Chatbot

    Description: Created an AI-powered chatbot for customer service using natural language processing and machine learning techniques. The chatbot was integrated into the client’s website and mobile app to provide 24/7 customer support.
    Technologies Used: Python, TensorFlow, Flask, JavaScript, Google Cloud Platform.
    Project Name: DevOps Automation

    Description: Led a project to automate the CI/CD pipeline for a large-scale application. Implemented automated testing, continuous integration, and continuous deployment using Jenkins, Docker, and Kubernetes.
    Technologies Used: Jenkins, Docker, Kubernetes, Git, Azure DevOps.
    Project Name: Real-Time Analytics Dashboard

    Description: Developed a real-time analytics dashboard for monitoring application performance and user engagement. The dashboard provided visualizations and insights using data from multiple sources.
    Technologies Used: Node.js, Express, D3.js, MongoDB, AWS.
    Professional Summary:
    Janvi Sungroya is a highly skilled and motivated Software Engineer with over 5 years of experience in developing, deploying, and maintaining software applications. He has a strong background in various programming languages, frameworks, and cloud platforms. Janvi Sungroya is passionate about leveraging cutting-edge technologies to create innovative solutions that meet business needs. He is a team player with excellent problem-solving skills and a commitment to continuous learning and improvement.
    """
referrer_college=f"College: {college_name}"
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/request_referral",methods=['GET','POST'])
def request_referral():
    if(request.method=='POST'):
        
        name = request.form['name']
        print("*****************")
        referral_contact=name
        referral_response = f"""Subject: Referral Request - Senior Sales Engineer (Job ID: 123) - Microsoft

    Dear {referral_contact},

    I hope this email finds you well.
    , and AWS. I'm particularly excited about the opportunity to contribute to Microsoft's cutting-edge work in cloud computing and AI, areas I've actively engaged with in projects like [Mention a relevant project from your profile, e.g., AI-Powered Chatbot or Cloud-Based Inventory Management System].

    I'm confident that my technical skills, combined with my collaborative approach and dedication to continuous learning, would make me a valuable asset to the team.

    Would you be willing to put my name forward for this position? I'd be happy to provide you with more information about my qualifications and discuss how my skills align with the role's requirements.

    Thank you for your time and consideration.

    Sincerely,

    John Doe"""
        referral_status1=""
        referral_status2=""
        referral_status3=""
        referral_status4=""
        referral_status5=""
        referral_status6=""
        referral_status7=""
        referral_status8=""
        referral_status9=""
        referral_status10=""
        if(name=='Sameer Rastogi'):referral_status1="Edit the Message"
        if(name=='Saharsh Jaiswal'):referral_status2="Edit the Message"
        if(name=='Harshal Shree'):referral_status3="Edit the Message"
        if(name=='Rashid Aziz'):referral_status4="Edit the Message"
        if(name=='Madhur Panwar'):referral_status5="Edit the Message"
        if(name=='Shanaya Gupta'):referral_status6="Edit the Message"
        if(name=='Sandeep Singh'):referral_status7="Edit the Message"
        if(name=='Mohan Lal Singh'):referral_status8="Edit the Message"
        if(name=='Satya Reddy'):referral_status9="Edit the Message"
        if(name=='Rohit Kumar'):referral_status10="Edit the Message"
        # referral_response =   genai_google.generate_referral_request(job_desc,user_profile,referral_contact,referrer_college)
        return render_template('referral_response.html', response=referral_response,referral_status1=referral_status1,referral_status2=referral_status2,referral_status3=referral_status3,referral_status4=referral_status4,referral_status5=referral_status5,referral_status6=referral_status6,referral_status7=referral_status7,referral_status8=referral_status8,referral_status9=referral_status9,referral_status10=referral_status10)
    return render_template('referral_response.html')



# @app.route("/request_referral_to_referrer",methods=['GET','POST'])
# def request_referral_to_referrer():
#     print(request.method)
#     if(request.method=='POST'):
#         name = request.form['name']
#         print("*****************")    
#         referral_contact=name
#         # referral_response =   genai_google.generate_referral_request(job_desc,user_profile,referral_contact)
#         referral_response = f"""Subject: Referral Request - Senior Sales Engineer (Job ID: 123) - Microsoft

#     Dear {referral_contact},

#     I hope this email finds you well.
#     , and AWS. I'm particularly excited about the opportunity to contribute to Microsoft's cutting-edge work in cloud computing and AI, areas I've actively engaged with in projects like [Mention a relevant project from your profile, e.g., AI-Powered Chatbot or Cloud-Based Inventory Management System].

#     I'm confident that my technical skills, combined with my collaborative approach and dedication to continuous learning, would make me a valuable asset to the team.

#     Would you be willing to put my name forward for this position? I'd be happy to provide you with more information about my qualifications and discuss how my skills align with the role's requirements.

#     Thank you for your time and consideration.

#     Sincerely,

#     John Doe"""
#         # print(referral_response)
#         return render_template('referral_response.html', response=referral_response)





if __name__=="__main__":
    with app.app_context():
    #  db.create_all()
     app.run(debug=True)
     
     
     
     
     
     
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///projectjanvisungroya.db'
# initialize the app with extension
# db=SQLAlchemy(app)

# # creating a database class sqlalchemy-used for making changes in database using python
# class project(db.Model):
#     sno= db.Column(db.Integer,primary_key=True)
#     name= db.Column(db.String(200),nullable=False)
#     email= db.Column(db.String(200),nullable=False)
#     dateCreated=db.Column(db.DateTime,default=datetime.now)
    
#     def __repr__(self) -> str:
#         return f"{self.sno}- {self.name}"
   
    
    
# @app.route("/",methods=['GET','POST'])
# def hello_world():
#     if(request.method=='POST'):
#          email= request.form["email"]
#          name= request.form["name"]
#          subProject1=project(name=name,email=email)
#          db.session.add(subProject1)
#          db.session.commit()
        
#     data=project.query.all()
#     return render_template('index.html',data=data)
    # for creating a single row
    # subProject1=project(name="Janvi",email="janvi@gmail30.com")
    # db.session.add(subProject1)
    # db.session.commit()
    

# @app.route("/delete/<int:sno>")
# def delete(sno):
#     recordToDelete=project.query.filter_by(sno=sno).first()
#     db.session.delete(recordToDelete)
#     db.session.commit()
#     return redirect("/")

# @app.route("/update/<int:sno>",methods=['POST','GET'])
# def update(sno):
#     print(request.method)
#     if(request.method=='POST'):
#         recordToUpdate=project.query.filter_by(sno=sno).first()
#         email= request.form["email"]
#         name=request.form["name"]
#         recordToUpdate.email=email
#         recordToUpdate.name=name
#         db.session.add(recordToUpdate)
#         db.session.commit()
#         return redirect("/")
    
#     recordToUpdate=project.query.filter_by(sno=sno).first()
#     return render_template('update.html',recordToUpdate=recordToUpdate)

# if __name__=="__main__":
#     with app.app_context():
#     #  db.create_all()
#      app.run(debug=True)
    # app.run(debug=True,port=8000)
    
    
# @app.route("/login", methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         return "post"
#     else:
#         return "<h1>This is products page<h1>"


# @app.route("/login/<username>")
# def showUser(username):
#     return render_template('app.html',username=username)

# @app.route("/login/<int:age>")
# def showUserAge(age):
#     print("Type of age-> ",type(age))
#     return "User age is "+str(age)