# Final Project Report

* Student Name: Tommer Ben-Joseph
* Github Username: Tommer-Roy
* Semester: Fall 2023
* Course: CS 5001



## Description 

For my project, I integrated the Flask library with my midterm project while building upon it with two additional cryptography algorithms. My final product is a web-based HTML cryptography application with the option of utilizing a subsitution, caesar, or atbash cipher algorithm. I chose this project because I believe that a core component of computer science, at least for me, is building things and being able to share them with anyone, and that includes people that may be less technologically savvy. Hosting my program in an HTML web app allows anyone with basic computer skills to easily use my product.

## Key Features

I incorporated the option to select from three different cryptography algorithms using a drop down menu, and also incorporated a drop down menu for the user to select whether he or she wants to decrypt or encrypt a message. I thought this was good functionality as it makes the application more user-friendly by eliminating a user error by way of typo. I thought this might be best practice given the situation, where there are a finite number of options to choose from. I would also consider the core aspect of the project to be a key feature, meaning the functionality to host my program on a web application.



## Guide

My project is quite user-friendly. Once navigating to the default Flask address (http://127.0.0.1:5000/), there are four objects that ask for user input. You must first select your cipher type in the drop down menu, then your action (decrypt/encrypt). Then you can input your message and optional key. Once you have completed these steps, simply hit submit.


## Installation Instructions

The first step is to ensure you have the Flask library installed on your machine. Enter `pip install flask` into the command line. After you have successfully installed flask, change your directory to where your app.py file is located via cd [path]. Then, in your command line type python app.py. If you have done everything correctly, you should receive the default locally hosted flask link (http://127.0.0.1:5000/). Enter this into your browser, and you should be able to use the app if everything is done correctly. It is important to also make sure your templates folder (which contain the HTML templates) should live in the same directory where the main driver (app.py) is located.

## Code Review

`shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))`

The above line took me a lot of trial and error to get right. While we haven't used modulo much in CS 5001, this ended up being the missing piece I needed to get my caesar_cipher function to work as intended. This allows the encryption to work accurately with a key that is greater than 26.

`if position >= 0 and position < len(key)`

The above line is something I added to the encrypt_message function that I did not initially have as part of my midterm submission. I needed to add this condition for cases where the user-provided key was too short, my program was returning IndexError: string index out of range. I was able to catch this while doing some edge case testing and added some methodology to ensure the program runs smoothly in this scenario.

```
@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        cipher_type = request.form.get("cipher_type")
        action = request.form.get("action")
        message = request.form.get("message")
        key = request.form.get("key")
```

Professor Lionelle pointed me in the right direction to help me get started on the above code, which was key for my project. Since the app is based in cryptography, it is important to ensure that it is handled through a POST request as opposed to GET. This ensures all components of the message stay private, as a GET request could cause some of the contents to get exposed in the web address.

### Major Challenges
I had zero prior experience with HTML formatting prior to this project, so I resorted to Google for some documentation on how to work with HTML formatting. It also took me quite a bit of time to understand how to properly set up and run my flask environment including how my directory needed to be structured regarding its relative path to app.py. I also had some difficulties incorporating the cipher type into result.html, as I wanted the user to also be able to get reminded of which cipher algorithm he or she chose after hitting submit incase he or she forgot. The most abstract concept initially, which ultimately casued this project to take much more time than I had initially forseen, was understanding how to make my app.py code communicate and flow into the form.html and result.html files. I ended up watching many flask tutorials on youtube in addition to some flask documentation that Professor Lionelle shared with me, which helped a lot.


## Example Runs

Please see the below youtube video that shows some screen recordings of me running my project.

https://www.youtube.com/watch?v=ZRSm56W6b_Y

## Testing

I tested my functions with doctests, and have saved the doctest results in a txt file in my GitHub repo. Additionally, I did ample edge case testing with the app itself. Unfortunately, because a large component of my project is rooted in Flask, I was not able to make test scripts for the actual application specifically. Nevertheless, I was able to successfully test my encryption and decryption functions using each algorithm, and I was also able to ensure that my app was up and running successfully.




## Missing Features / What's Next
I would have liked to add some formatting to make the application more aesthetically pleasing. Additionally, I believe the app could be made to be more robust and incorporate many more different encryption algorithms. I also believe if I had more time, I could have experimented with actually hosting the app on a web server, allowing anyone to access the encryption app using just the link to the website. I also think some potentially interesting features could include a section where you can send your encrypted message to anyone by inputting their email address, and the email would also include a link to the app for decryption. It would also ideally include a summary page about each encryption algorithm that would discuss the pros and cons of each algo. This may be a personal project that I would like to work on, as I do find cybersecurity intriguing and would like to dive into the field a bit more.

## Final Reflection
I have had a great experience in Professor Lionelle's CS 5001 class. My experience certainly affirmed my decision to pursure a masters in Computer Science at Northeastern.  Previously, I had dabbled a bit with Python and was able to write simple functions, but in this class, I am learning how to build, design, and might I say engineer.  This class has allowed me to cross the bridge into actually designing some useful tools in a manner that is conductive to a productive workplace. I am learning how to write code that is reusable, scalable, readable, clean etc. and I have started to incorporate Python into my workflow in the office in a manner that was previously thought to be unattainable. It has allowed me to be much more efficient and productive at work, as I am able to "automate the boring stuff" while also leveraging my newfound skillset on some other interesting work.

In order to keep learning more, I need to stay hungry for knowledge and keep an open mind. I also find it very helpful to collaborate with fellow classmates in the team activities. Furthermore, it can be very helpful to discuss different approaches to the same problem, as it allows your brain to draw connections to how other algorithms may also work.  Additionally, it is very important to allow yourself to take breaks when needed and not get too hung up when you are stuck on a problem. Remembering that rule has certainly allowed me to keep my sanity in check, especially when working on some tough programs earlier in the semester before I started to get the hang of it. Most importantly, code review has been key. I find it interesting to go back through my old assignments, and think to myself how I may have approached the assignment differently with some of the newer concepts I had learned.  In summary, I have greatly enjoyed my time in Professor Lionelle's class and I look forward to learning more from him in the future.  I am thrilled to see what new heights this skill set will enable me to reach, both on a professional and personal level.
