import dash
from dash import dcc, html

layout = html.Div(
    [
        html.H1('Welcome to Social Media Analysis Dashboard!'),
        html.Hr(),
        html.P('Unlock the power of data-driven insights for your LinkedIn profile with our innovative platform. Our web application empowers you to gain valuable analytics and insights into your LinkedIn presence, allowing you to make informed decisions to enhance your professional brand.'),
        html.P("With SOCIAL MEDIA ANALYSIS DASHBOARD, you can seamlessly upload your LinkedIn profile data and delve into comprehensive analytics tailored to your profile's performance. Whether you're a job seeker, recruiter, or simply aiming to boost your professional visibility, our tools provide invaluable insights to help you achieve your goals."),
        html.Hr(),
        html.H4("Key Features"),
        html.P("1. LinkedIn Profile Analytics: Gain deep insights into your LinkedIn profile's performance metrics, including profile views, engagement, network growth, and more. Understand what resonates with your audience and optimize your profile accordingly."),
        html.P("2. Custom Data Upload: Seamlessly upload additional data sets to complement your LinkedIn analytics. Whether it's your resume, portfolio, or other relevant documents, integrate them into our platform for a holistic analysis of your professional presence."),
        html.P("3. Data Visualization: Visualize your analytics through intuitive graphs, charts, and dashboards. Easily interpret complex data to identify trends, strengths, and areas for improvement."),
        html.P("4. Competitor Analysis: Benchmark your LinkedIn profile against industry peers and competitors. Gain valuable insights into best practices and opportunities for differentiation."),
        html.P("5. Actionable Recommendations: Receive personalized recommendations based on your analytics to optimize your LinkedIn profile effectively. From profile enhancements to content strategies, empower yourself with actionable insights."),
        html.P("6. Privacy and Security: Rest assured that your data privacy and security are our top priorities. We employ robust encryption and strict security measures to safeguard your information at all times."),
        html.Hr(),
        html.P("Whether you're a seasoned professional or just starting your career journey, SOCIAL MEDIA ANALYSIS DASHBOARD is your go-to solution for unlocking the full potential of your LinkedIn profile. Take control of your professional brand like never before!", style={'font-weight': 'bold'}),
    ],
    style={'textAlign': 'center', 'font-size': '20px'}
)

