<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nutrition Agent README</title>
</head>
<body>
    <h1>Nutrition Agent</h1>

    <h2>Overview</h2>
    <p>
        The <strong>Nutrition Agent</strong> is a multi-modal agent designed to provide nutritional benefits and insights about the product. 
        This agent utilizes the <strong>Phidata framework</strong>, which can build multi-modal agents with memory, knowledge, tools, and reasoning. 
        This will help users find detailed information about the nutrition of the food they consume.
    </p>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#what-is-phidata">What is Phidata?</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
    </ul>

    <h2 id="what-is-phidata">What is Phidata?</h2>
    <p>
        Phidata is a framework for building multi-modal agents. Use Phidata to:
    </p>
    <ul>
        <li>Build multi-modal agents with memory, knowledge, tools, and reasoning.</li>
        <li>Build teams of agents that can work together to solve problems.</li>
        <li>Chat with your agents using a beautiful Agent UI.</li>
    </ul>

    <h2 id="features">Features</h2>
    <h3>Image-Based Ingredient Analysis</h3>
    <ul>
        <li>Upload an image of a food item, and the application will:
            <ul>
                <li>Analyze the image to identify ingredients.</li>
                <li>Provide detailed nutritional information for each ingredient.</li>
                <li>Highlight any harmful or less desirable ingredients.</li>
            </ul>
        </li>
    </ul>

    <h3>Smart Food Alternatives</h3>
    <ul>
        <li>Suggest healthier alternatives if the identified food item has poor nutritional value.</li>
    </ul>

    <h2 id="project-structure">Project Structure</h2>
    <pre>
nutrition-agent/
│
├── images/
│   ├── maggi_pack image/         # sample images that can be used
│   ├── peanut butter image/      
│
├── training/                     # system prompt and instructions for the agent to work
│
├── data/                         # Sample data and datasets
│
├── docs/                         # Documentation and resources
│
├── requirements.txt              # Python dependencies
│
└── README.md                     # Project documentation
    </pre>
</body>
</html>


