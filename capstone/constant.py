ICONS = {
    "dashboard": "fa-solid fa-gauge-high",
    "category": "fa-solid fa-grip",
    "add": "fa-solid fa-circle-plus",
    "list": "fa-regular fa-file-lines",
    "questionnaire": "fa-regular fa-rectangle-list",
    "result": "fa-solid fa-users",
    "notification": "fa-solid fa-bell",
    "detail": "fa-solid fa-file-pen",
    "profile": "fa-solid fa-id-card"
}

SOFTSKILLS = (
    ['E', 'CO'],
    ['F', 'IN'],
    ['T', 'AP'],
    ['P', 'OA'],
    ['J', 'OR'],
    ['F', 'TP'],
    ['I', 'AW'],
    ['F', 'AL'],
    ['I', 'IM'],
    ['S', 'PT'],
    ['P', 'FL']
)

PERSONAlITY_TYPES = {
    0: "INTP",
    1: "ISTP",
    2: "ENTP",
    3: "ESTP",
    4: "INFP",
    5: "ISFP",
    6: "ENFP",
    7: "ESFP",
    8: "INTJ",
    9: "ISTJ",
    10: "ENTJ",
    11: "ESTJ",
    12: "INFJ",
    13: "ISFJ",
    14: "ENFJ",
    15: "ESFJ"
}

MBTI_QUESTIONNAIRE_VALUE = {
    1: ["For my free time, I ideally prefer to attend social activities and events where i can be surrounded by people, meet and talk to new people.", "For my free time, I like to be alone and enjoy some quiet time by myself."],
    2: ["I like hobbies that are technical and hands on.", "I am interested in hobbies that allow me to use my intuition to explore abstract concepts and use my imagination to dream big."],
    3: ["My favorite hobbies are those that allow me to learn new things.", "I tend to prioritize personal values and harmony over cold logic."],
    4: ["It's more exciting for me to jump into something without a clear plan than to follow a set path.", "I like for my holidays to have everything being organized and booked in advance so that i can enjoy everything without worrying."]
}

ROLE_PREFERENCES = {
    "Software Analyst": {"T": 21, "P": 21, "F": 10.5, "S": 15.8, "E": 10.5, "J": 10.5, "I": 10.5},
    "Software Designer": {"T": 21, "F": 36.8, "E": 10.5, "J": 10.5, "N": 10.5, "S": 10.5},
    "Programmer": {"T": 50, "E": 25, "F": 25},
    "Software Tester": {"T": 26.3, "E": 15.8, "J": 15.8, "F": 31.6, "S": 10.5},
    "Software Maintainer": {"T": 40, "F": 40, "P": 20},
}

SKILL_TO_MBTI = {
    "Effective Communicative": "E",
    "Interpersonal Aptitude": "F",
    "Analytical & Problem-solving Approach": "T",
    "Openness to Changes": "P",
    "Managerial/Operational Skills": "J",
    "Team Work Aptitude": "F",
    "Work Independence Aptitude": "I",
    "Listing Skills": "F",
    "Inventive Mind": "N",
    "Pay Critical Attention to Facts": "S",
    "Fast Learning Aptitude": "P"
}

ANALYST_TASKS_DESC = {
    0: "Liaising extensively with external or internal clients",
    1: "Analyzing clients’ existing systems",
    2: "Translating client requirements into highly specified project briefs",
    3: "Identifying options for potential solutions, assessing them for both technical and business suitability",
    4: "Creating logical and innovative solutions to complex problems",
    5: "Drawing up specific proposals for modified or replacement systems",
    6: "Producing project feasibility reports",
    7: "Working closely with developers and a variety of end users to ensure technical compatibility and user satisfaction",
    8: "Overseeing the implementation of a new system",
    9: "Planning ahead and working flexibly to a deadline",
    10: "Keeping up to date with technical and industry sector development"
}

ANALYST_TASKS_REQ = {
    0: ["Effective Communicative", "Interpersonal Aptitude"],
    1: ["Analytical & Problem-solving Approach", "Pay Critical Attention to Facts"],
    2: ["Effective Communicative", "Fast Learning Aptitude"],
    3: ["Analytical & Problem-solving Approach", "Openness to Changes"],
    4: ["Inventive Mind", "Analytical & Problem-solving Approach"],
    5: ["Listing Skills", "Managerial/Operational Skills"],
    6: ["Analytical & Problem-solving Approach", "Pay Critical Attention to Facts"],
    7: ["Team Work Aptitude", "Interpersonal Aptitude"],
    8: ["Managerial/Operational Skills", "Work Independence Aptitude"],
    9: ["Openness to Changes", "Work Independence Aptitude"],
    10: ["Fast Learning Aptitude", "Pay Critical Attention to Facts"]
}

DESIGNER_TASKS_DESC = {
    0: "Having the ability to craft scenarios, storyboards, information architecture, features, and interfaces",
    1: "Collaborating closely with management, engineers, and fellow designers to evaluate and iterate on ideas and designs",
    2: "Prototyping user experience and design ideas",
    3: "Keeping up to date with technical and industry sector developments",
    4: "Understanding business opportunities and assisting project team with respect to architecture of the technical solution",
    5: "Creating an architectural design with the necessary specifications for the hardware, software, and data",
    6: "Working closely with system users to ensure that implementation meets customer requirements and is aligned to the system’s technical architecture",
    7: "Developing, documenting, and revising system design procedures",
    8: "Participating in testing and evaluating system functionality to ensure successful integration",
    9: "Determining hardware, software, and network requirements of the software system",
    10: "Assisting with system analyses; cost and bidding activities"
}

DESIGNER_TASKS_REQ = {
    0: ["Inventive Mind", "Listing Skills"],
    1: ["Team Work Aptitude", "Interpersonal Aptitude"],
    2: ["Inventive Mind", "Analytical & Problem-solving Approach"],
    3: ["Fast Learning Aptitude", "Openness to Changes"],
    4: ["Effective Communicative", "Analytical & Problem-solving Approach"],
    5: ["Listing Skills", "Pay Critical Attention to Facts"],
    6: ["Interpersonal Aptitude", "Team Work Aptitude"],
    7: ["Pay Critical Attention to Facts", "Managerial/Operational Skills"],
    8: ["Analytical & Problem-solving Approach", "Work Independence Aptitude"],
    9: ["Analytical & Problem-solving Approach", "Listing Skills"],
    10: ["Managerial/Operational Skills", "Effective Communicative"]
}

PROGRAMMER_TASKS_DESC = {
    0: "Participates in development efforts; elaborates and documents all business-related applications",
    1: "Analyzes business requirements for system subcomponents and prepares detailed programming specifications for assigned system applications",
    2: "Formulates test cases to test application software in development, to ensure a program’s functionality matches its specification’s business requirements and to ensure the company’s programming standards are followed",
    3: "Analyzes technical specifications; builds and implements functionally accurate and modular application programs according to approved design specifications",
    4: "Coordinates programming tasks, team members, and projects within the department",
    5: "Determines forms, procedures, and other documentation needed for installation and maintenance of application programs",
    6: "Translates detailed flow charts into coded machine instructions and confers with technical personnel in planning programs",
    7: "Selects and incorporates available software programs"
}

PROGRAMMER_TASKS_REQ = {
    0: ["Effective Communicative", "Listing Skills"],
    1: ["Analytical & Problem-solving Approach", "Pay Critical Attention to Facts"],
    2: ["Analytical & Problem-solving Approach", "Attention to Detail"],
    3: ["Inventive Mind", "Analytical & Problem-solving Approach"],
    4: ["Managerial/Operational Skills", "Team Work Aptitude"],
    5: ["Listing Skills", "Analytical & Problem-solving Approach"],
    6: ["Effective Communicative", "Fast Learning Aptitude"],
    7: ["Openness to Changes", "Work Independence Aptitude"]
}

TESTER_TASKS_DESC = {
    0: "Coordinates necessary testing resources to ensure completion by deadlines",
    1: "Gathers test requirements and produces test specifications",
    2: "Performs manual execution of tests, records results, and investigates and logs results",
    3: "Manages and supports the team in creating usable test assets for both manual and automated test scripts",
    4: "Demonstrates ability to define and implement medium-to-large-scale test plans and strategies according to quality objectives, project timelines, and resources",
    5: "Manages defects, including the identification, logging, tracking, triaging, and verification of issues",
    6: "Identifies and mitigates business and technical risks in the development and execution of the test strategy",
    7: "Analyzes and evaluates, documents, and communicates testing progress for stakeholders",
    8: "Ensures test progress, methodologies, and tools are applied appropriately and that test phase entry/exit criteria are agreed to by stakeholders and applied by the test team",
    9: "Maintains relevant test results databases",
    10: "Communicates and negotiates testing timelines, budget, staffing, scope, and critical milestones with project managers"
}

TESTER_TASKS_REQ = {
    0: ["Managerial/Operational Skills", "Team Work Aptitude"],
    1: ["Analytical & Problem-solving Approach", "Listing Skills"],
    2: ["Pay Critical Attention to Facts", "Analytical & Problem-solving Approach"],
    3: ["Team Work Aptitude", "Inventive Mind"],
    4: ["Managerial/Operational Skills", "Analytical & Problem-solving Approach"],
    5: ["Pay Critical Attention to Facts", "Work Independence Aptitude"],
    6: ["Analytical & Problem-solving Approach", "Effective Communicative"],
    7: ["Effective Communicative", "Interpersonal Aptitude"],
    8: ["Managerial/Operational Skills", "Analytical & Problem-solving Approach"],
    9: ["Listing Skills", "Fast Learning Aptitude"],
    10: ["Effective Communicative", "Interpersonal Aptitude"]
}

MAINTAINER_TASKS_DESC = {
    0: "Provide, maintain, or update systems documentation to reflect new applications or enhancements to existing applications",
    1: "Provide skills transfer or assistance to junior development team members to improve product quality and performance and to ensure standards are implemented",
    2: "Regularly coordinate or take part in discussions with users and system analysts in developing and maintaining applications or enhancements to meet business needs",
    3: "Contribute to process-improvement initiatives, especially with regard to programming and IT",
    4: "Manage and support the maintenance of systems developed in-house as directed by the system analyst or the manager, including trouble-shooting, reporting problems, and recommending, designing, and implementing sound solutions",
    5: "Comply with mandated policies and procedures and contribute to procedural improvements",
    6: "Coordinate system integration testing and participate in user acceptance testing",
    7: "Be willing to learn new technologies and keep on top of emerging trends in application development; have an open mind to consider different approaches to solving technical problems"
}

MAINTAINER_TASKS_REQ = {
    0: ["Listing Skills", "Pay Critical Attention to Facts"],
    1: ["Interpersonal Aptitude", "Team Work Aptitude"],
    2: ["Effective Communicative", "Interpersonal Aptitude"],
    3: ["Analytical & Problem-solving Approach", "Openness to Changes"],
    4: ["Analytical & Problem-solving Approach", "Managerial/Operational Skills"],
    5: ["Analytical & Problem-solving Approach", "Work Independence Aptitude"],
    6: ["Team Work Aptitude", "Analytical & Problem-solving Approach"],
    7: ["Openness to Changes", "Fast Learning Aptitude", "Inventive Mind"]
}

# ANALYST_TASKS_REQ = {
#     "Liaising extensively with external or internal clients": ["Effective Communicative", "Interpersonal Aptitude"],
#     "Analyzing clients’ existing systems": ["Analytical & Problem-solving Approach", "Pay Critical Attention to Facts"],
#     "Translating client requirements into highly specified project briefs": ["Effective Communicative", "Fast Learning Aptitude"],
#     "Identifying options for potential solutions, assessing them for both technical and business suitability": ["Analytical & Problem-solving Approach", "Openness to Changes"],
#     "Creating logical and innovative solutions to complex problems": ["Inventive Mind", "Analytical & Problem-solving Approach"],
#     "Drawing up specific proposals for modified or replacement systems": ["Listing Skills", "Managerial/Operational Skills"],
#     "Producing project feasibility reports": ["Analytical & Problem-solving Approach", "Pay Critical Attention to Facts"],
#     "Working closely with developers and a variety of end users to ensure technical compatibility and user satisfaction": ["Team Work Aptitude", "Interpersonal Aptitude"],
#     "Overseeing the implementation of a new system": ["Managerial/Operational Skills", "Work Independence Aptitude"],
#     "Planning ahead and working flexibly to a deadline": ["Openness to Changes", "Work Independence Aptitude"],
#     "Keeping up to date with technical and industry sector development": ["Fast Learning Aptitude", "Pay Critical Attention to Facts"]
# }

# DESIGNER_TASKS_REQ = {
#     "Having the ability to craft scenarios, storyboards, information architecture, features, and interfaces": ["Inventive Mind", "Listing Skills"],
#     "Collaborating closely with management, engineers, and fellow designers to evaluate and iterate on ideas and designs": ["Team Work Aptitude", "Interpersonal Aptitude"],
#     "Prototyping user experience and design ideas": ["Inventive Mind", "Analytical & Problem-solving Approach"],
#     "Keeping up to date with technical and industry sector developments": ["Fast Learning Aptitude", "Openness to Changes"],
#     "Understanding business opportunities and assisting project team with respect to architecture of the technical solution": ["Effective Communicative", "Analytical & Problem-solving Approach"],
#     "Creating an architectural design with the necessary specifications for the hardware, software, and data": ["Listing Skills", "Pay Critical Attention to Facts"],
#     "Working closely with system users to ensure that implementation meets customer requirements and is aligned to the system’s technical architecture": ["Interpersonal Aptitude", "Team Work Aptitude"],
#     "Developing, documenting, and revising system design procedures": ["Pay Critical Attention to Facts", "Managerial/Operational Skills"],
#     "Participating in testing and evaluating system functionality to ensure successful integration": ["Analytical & Problem-solving Approach", "Work Independence Aptitude"],
#     "Determining hardware, software, and network requirements of the software system": ["Analytical & Problem-solving Approach", "Listing Skills"],
#     "Assisting with system analyses; cost and bidding activities": ["Managerial/Operational Skills", "Effective Communicative"]
# }

# PROGRAMMER_TASKS_REQ = {
#     "Participates in development efforts; elaborates and documents all business-related applications": ["Effective Communicative", "Listing Skills"],
#     "Analyzes business requirements for system subcomponents and prepares detailed programming specifications for assigned system applications": ["Analytical & Problem-solving Approach", "Pay Critical Attention to Facts"],
#     "Formulates test cases to test application software in development, to ensure a program’s functionality matches its specification’s business requirements and to ensure the company’s programming standards are followed": ["Analytical & Problem-solving Approach", "Attention to Detail"],
#     "Analyzes technical specifications; builds and implements functionally accurate and modular application programs according to approved design specifications": ["Inventive Mind", "Analytical & Problem-solving Approach"],
#     "Coordinates programming tasks, team members, and projects within the department": ["Managerial/Operational Skills", "Team Work Aptitude"],
#     "Determines forms, procedures, and other documentation needed for installation and maintenance of application programs": ["Listing Skills", "Analytical & Problem-solving Approach"],
#     "Translates detailed flow charts into coded machine instructions and confers with technical personnel in planning programs": ["Effective Communicative", "Fast Learning Aptitude"],
#     "Selects and incorporates available software programs": ["Openness to Changes", "Work Independence Aptitude"]
# }

# TESTER_TASKS_REQ = {
#     "Coordinates necessary testing resources to ensure completion by deadlines": ["Managerial/Operational Skills", "Team Work Aptitude"],
#     "Gathers test requirements and produces test specifications": ["Analytical & Problem-solving Approach", "Listing Skills"],
#     "Performs manual execution of tests, records results, and investigates and logs results": ["Pay Critical Attention to Facts", "Analytical & Problem-solving Approach"],
#     "Manages and supports the team in creating usable test assets for both manual and automated test scripts": ["Team Work Aptitude", "Inventive Mind"],
#     "Demonstrates ability to define and implement medium-to-large-scale test plans and strategies according to quality objectives, project timelines, and resources": ["Managerial/Operational Skills", "Analytical & Problem-solving Approach"],
#     "Manages defects, including the identification, logging, tracking, triaging, and verification of issues": ["Pay Critical Attention to Facts", "Work Independence Aptitude"],
#     "Identifies and mitigates business and technical risks in the development and execution of the test strategy": ["Analytical & Problem-solving Approach", "Effective Communicative"],
#     "Analyzes and evaluates, documents, and communicates testing progress for stakeholders": ["Effective Communicative", "Interpersonal Aptitude"],
#     "Ensures test progress, methodologies, and tools are applied appropriately and that test phase entry/exit criteria are agreed to by stakeholders and applied by the test team": ["Managerial/Operational Skills", "Analytical & Problem-solving Approach"],
#     "Maintains relevant test results databases": ["Listing Skills", "Fast Learning Aptitude"],
#     "Communicates and negotiates testing timelines, budget, staffing, scope, and critical milestones with project managers": ["Effective Communicative", "Interpersonal Aptitude"]
# }
#
# MAINTAINER_TASKS_REQ = {
#     "Provide, maintain, or update systems documentation to reflect new applications or enhancements to existing applications": ["Listing Skills", "Pay Critical Attention to Facts"],
#     "Provide skills transfer or assistance to junior development team members to improve product quality and performance and to ensure standards are implemented": ["Interpersonal Aptitude", "Team Work Aptitude"],
#     "Regularly coordinate or take part in discussions with users and system analysts in developing and maintaining applications or enhancements to meet business needs": ["Effective Communicative", "Interpersonal Aptitude"],
#     "Contribute to process-improvement initiatives, especially with regard to programming and IT": ["Analytical & Problem-solving Approach", "Openness to Changes"],
#     "Manage and support the maintenance of systems developed in-house as directed by the system analyst or the manager, including trouble-shooting, reporting problems, and recommending, designing, and implementing sound solutions": ["Analytical & Problem-solving Approach", "Managerial/Operational Skills"],
#     "Comply with mandated policies and procedures and contribute to procedural improvements": ["Analytical & Problem-solving Approach", "Work Independence Aptitude"],
#     "Coordinate system integration testing and participate in user acceptance testing": ["Team Work Aptitude", "Analytical & Problem-solving Approach"],
#     "Be willing to learn new technologies and keep on top of emerging trends in application development; have an open mind to consider different approaches to solving technical problems": ["Openness to Changes", "Fast Learning Aptitude", "Inventive Mind"]
# }