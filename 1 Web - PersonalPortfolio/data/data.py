#SRI Invoice Downloader & Reporter
projects = [
     {
        "name": "Electronic Invoicing & Inventory Management System",
        "description": '''
        Developing an end-to-end electronic invoicing and inventory management system for a local bar. Responsible for the entire development lifecycle, from database design and system architecture to backend and frontend development. Built secure REST APIs with JWT authentication, Pydantic validation, and SQLAlchemy, while developing a modern React interface for managing business operations and inventory. Designed the system as a scalable foundation for automating core business processes and supporting future integrations.
        ''',
        "img_url": [f"project5-{i}.png" for i in range(1, 5)],
        "technologies": ["Python", "FastAPI", "React", "TypeScript", "PostgreSQL", "SQLAlchemy", "CSS"],
     },
     {
        "name": "Event Ticket Booking Platform",
        "description": ''' Built the backend of an event ticket booking platform for events in Colombia. Implemented JWT authentication, Google login, Mercado Pago payments, file uploads, shopping cart, coupon management, and an assistant chat system. Developed the API with a team of three backend developers.''',
        "img_url": [f"project4-{i}.png" for i in range(1, 6)],
        "technologies": ["Express.js", "TypeScript", "TypeORM", "PostgreSQL", "JWT", "Mercado Pago"],
     },
    {
        "name": "Population Evolution Analysis — Cotopaxi, Ecuador",
        "description": '''
        Analyzed population census data from Ecuador (1990–2010) to study demographic changes across the province of Cotopaxi. Worked with large-scale datasets, applying data cleaning, transformation, exploratory analysis, and statistical techniques to extract meaningful patterns and trends. Developed geospatial visualizations using gvSIG to represent population evolution across the province and support the interpretation of demographic data.
        ''',
        "img_url": [f"project3-{i}.png" for i in range(1,7)],
        "technologies": ["Python", "Pandas", "NumPy", "Matplotlib", "Big Data", "Data Analysis", "Statistics", "Geospatial Visualization"],
     },
    {
        "name": "SRI Invoice Automation System",
        "description": '''
        Developed a software solution to automate the retrieval and management of electronic invoices through the SRI web service. The system automatically downloads invoice information, generates the corresponding PDF documents, and organizes them into folders according to the billing month.
        
        The application also processes the collected information to generate a tax reporting file, providing a structured summary of the invoices and amounts required to complete the corresponding tax declaration through the SRI online portal. This significantly reduces manual data entry and simplifies the process of managing and preparing electronic invoices for tax reporting.
        ''',
        "img_url": [f"project2-{i}.png" for i in range(1,5)],
        "technologies": ["Python", "Qt", "Web Services/SOAP", "XML", "PDF generatión", "Data processing", "Automation"],
    },
    {
        "name": "A Low Cost Robotic Medical Simulator for CPR Training",
        "description": '''
        Developed the <strong>software architecture</strong> and <strong>real-time monitoring system</strong> for a robotic medical simulator designed for <strong>cardiopulmonary resuscitation training</strong>. The system was implemented using <strong>Python</strong> connecting via <strong>TCP/IP</strong> with a <strong>Raspberry Pi</strong>, integrating multiple <strong>sensors and actuators</strong> to monitor and control the simulator in real time.
        <br><br>
    
        The software <strong>acquires and processes sensor data in real time</strong> to evaluate CPR performance, controls actuators to simulate physiological responses, and enables real-time visualization and <strong>generation of ECG waveforms and cardiac rhythms</strong>. It also allows configure and execute clinical scenarios with immediate feedback .<br><br>
    
        The project resulted in a <strong>peer-reviewed scientific publication</strong>: <em>A Low Cost Robotic Medical Simulator for CPR Training</em>, published in <a href="https://doi.org/10.1088/1757-899X/575/1/012019" style="color: #0fc3ff; text-decoration: underline;">IOP Conference Series: Materials Science and Engineering (2019)</a>.
        ''',
        "img_url": [f"project1-{i}.png" for i in range(1,9)],
        "technologies": ["Python", "Qt", "Numpy", "Raspberry Pi", "PyQtGraph", "Real-Time Data Acquisition", "Sensors & Actuators", "TCP/IP"],
    },
]
