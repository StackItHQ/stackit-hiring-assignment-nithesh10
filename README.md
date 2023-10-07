
# StackIt Hiring Assignment

### Welcome to StackIt's hiring assignment! 🚀

**If you didn't get here through github classroom, are you sure you're supposed to be here? 🤨**


We are glad to have you here, but before you read what you're going to beat your head over for the next few hours (maybe days?), let's get a few things straight:
- We really appreciate honesty. Don't copy anyone else's assignment, it'll only sabotage your chances :P
- You're free to use any stack, and library of your choice. Use whatever you can get your hands on, on the internet!
- We love out of the box solutions. We prefer to call it *Jugaad* 
- This might be just the first round, but carries the most importance of all. Give your best, and we hope you have a fun time solving this problem.

## ✨ **Problem Statement: Crafting a CSV Importer for Google Sheets** ✨

**Context**:
Data analysts around the world 🌍, handle massive amounts of data to derive meaningful insights for their organization 📊. Among the tools they use, Google Sheets 📈 stands out due to its ease of use, accessibility, and collaborative features. However, many analysts have identified a recurring pain point: the cumbersome process of importing CSV files into Google Sheets repeatedly.

A typical week of an analyst in an e-commerce company 🛒 involves receiving multiple CSV files 📁 containing sales, inventory, customer feedback, and more. The data from these files needs to be meticulously analyzed and presented in the company’s weekly meetings. However, instead of diving directly into analysis, most analysts need to spend an inordinate amount of time just importing and structuring these CSV files into Google Sheets ⏳. This repetitive, time-consuming task reduces the efficiency of these professionals and delays the extraction of crucial insights 😫.

**Today, you are going to make their lives better.**

**Problem Statement**:
Make a CSV Importer for Google Sheets that lets users drag and drop CSV files onto the Google Sheet. The moment they drop the CSV file, allow them to select which columns to import 🗂️.

You get brownie points 🍪 if you can make it even easier by allowing them to filter the data as well before importing it into Google Sheets 🔍.

**Other pointers**:
- Import to Sheet – After validation and mapping, devise a method to populate the data into a chosen Google Sheet, either appending to existing data or creating a new sheet 📥📋.
- Optimize for Large Files – Large datasets are common in analytics. Your solution should effectively handle large CSV files (~15MB CSV file) without causing performance issues or prolonged waiting times 📈📦.

## Submission ⏰
The timeline for this submission is: **9AM, 30th Sept, 2023 - 12PM, 2nd Oct, 2023**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)

Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [ ✔️] My code's working just fine! 🥳
- [✔️ ] I have recorded a video showing it working and embedded it in the README ▶️
- [✔️ ] I have tested all the normal working cases 😎
- [✔️ ] I have even solved some edge cases (brownie points) 💪
- [✔️ ] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓




Feel free to check the discussions tab, you might get something of help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore 😛

## Developer's Section
https://github.com/StackItHQ/stackit-hiring-assignment-nithesh10/assets/83530216/2ebaa42e-5e58-4249-87a3-94bfe4069283

### Roadmap

1. **Setup Flask Project**
    ```
    csv_importer/
    ├── app/
    │   ├── __init__.py
    │   ├── routes.py
    │   └── templates/
    │       ├── base.html
    │       └── upload.html
    ├── venv/
    ├── config.py
    ├── run.py
    └── README.md
    ```

2. **Google Sheets API**
    - Set up Google Cloud project.
    - Enable Google Sheets API.
    - Generate OAuth 2.0 credentials.

3. **Backend**
    - Implement file upload route.
    - Parse uploaded CSV files.
    - Allow column selection and data filtering.
    - Integrate with Google Sheets API.

4. **Frontend**
    - Create a user-friendly interface.
    - Implement drag-and-drop file uploads.
    - Create UI for column selection and filtering.

5. **Production Checklist**
    - Optimize for large CSV files ✔️
    - Test with different file sizes ✔️
    - Ensure column selection and filtering work ✔️
    - Documentation ✔️
    - Video Recording ✔️

### Approach

**Technology Stack:** I chose to build this project using Flask, a lightweight and flexible web framework for Python. Additionally, I used HTML, CSS, and JavaScript for the frontend to create a user-friendly interface.

**Design Decisions:**
- **User Interface:** I designed a simple and intuitive user interface using HTML and CSS. Users can drag and drop CSV files onto the web application, making it easy and familiar for them.
- **Backend Processing:** When a user drops a CSV file, the Flask backend handles file upload, validates the CSV, and presents the user with options to select columns for import. I designed this flow to be step-by-step and user-friendly.
- **CSV Import to Google Sheets:** To import data into Google Sheets, I used the Google Sheets API, and I provided users with the option to either append data to an existing sheet or create a new one.
- **Error Handling:** I implemented robust error handling to provide clear feedback to users in case of issues such as invalid CSV files or API errors.

**Challenges:**
- **Performance:** Optimizing the application to handle large CSV files without causing performance issues was a concern. I implemented efficient data processing to mitigate this.

**Features:**
- **Drag-and-Drop:** Users can easily upload CSV files by dragging and dropping them onto the web application.
- **Column Mapping:** Users have the option to map CSV columns to Google Sheets columns, ensuring flexibility in data import.
- **Data Filtering (Brownie Points):** I added a feature that allows users to filter data before importing it into Google Sheets. This can help streamline the import process and reduce unnecessary data.

**Testing:** I thoroughly tested the application to ensure its functionality and reliability. Test cases included:
- Uploading valid and invalid CSV files.
- Testing various column mapping scenarios.
- Importing data into existing and new Google Sheets.
- Performance testing with large CSV files to ensure the application remains responsive.

**Final Thoughts:** Building this CSV Importer for Google Sheets using Flask was a rewarding experience. It addresses a practical problem faced by data analysts and offers a user-friendly solution. I enjoyed the challenge of integrating with the Google Sheets API and ensuring the application's reliability and performance. This project has reinforced my skills in web development, API integration, and user interface design.

### Checklist
- [x] My code's working just fine! 🥳
- [x] I have recorded a video showing it working and embedded it in the README ▶️
- [x] I have tested all the normal working cases 😎
- [x] I have even solved some edge cases (brownie points) 💪
- [x] I added my very planned-out approach to the problem at the end of this README 📜
