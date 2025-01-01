# Nutrition Agent

## Overview

The **Nutrition Agent** is a multi-modal agent designed to provide nutritional benefits and insights about the product.  
This agent utilizes the **Phidata framework**, which can build multi-modal agents with memory, knowledge, tools, and reasoning.  
This will help users find detailed information about the nutrition of the food they consume.

## Table of Contents

- [What is Phidata?](#what-is-phidata)
- [Features](#features)
- [Project Structure](#project-structure)

## What is Phidata?

Phidata is a framework for building multi-modal agents. Use Phidata to:

- Build multi-modal agents with memory, knowledge, tools, and reasoning.
- Build teams of agents that can work together to solve problems.
- Chat with your agents using a beautiful Agent UI.

## Features

### Image-Based Ingredient Analysis

- Upload an image of a food item, and the application will:
  - Analyze the image to identify ingredients.
  - Provide detailed nutritional information for each ingredient.
  - Highlight any harmful or less desirable ingredients.

### Smart Food Alternatives

- Suggest healthier alternatives if the identified food item has poor nutritional value.

## Project Structure

nutrition-agent/ │ ├── images/ │ ├── maggi_pack image/ # Sample images that can be used │ ├── peanut butter image/
│ ├── training/ # System prompt and instructions for the agent to work │ ├── data/ # Sample data and datasets │ ├── docs/ # Documentation and resources │ ├── requirements.txt # Python dependencies │ └── README.md # Project documentation
