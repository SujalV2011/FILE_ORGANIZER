import os  
import shutil  
  
# Define the source directory containing the files to be organized  
# Taking raw input which won't interpret escape characters  
source_dir = input(r"Enter the source directory path : ").replace('\\', '/')  
  
# Define the destination directory where the organized files will be moved to  
# Taking raw input which won't interpret escape characters  
dest_dir = input(r"Enter the destination directory path : ").replace('\\', '/')  
  
# Create a dictionary to map file extensions to their respective folders  
extension_map = {  
    '.jpg': 'Images',  
    '.png': 'Images',  
    '.gif': 'Images',  
    '.jpeg': 'Images',  
    '.pdf': 'PDF Files',  
    '.txt': 'Text Files',  
    '.docx': 'Word Document',  
    '.rtf': 'Word Document',  
    '.xlsx': 'Excel Files',  
    '.pptx': 'PowerPoint Persentations',  
    '.ppt': 'PowerPoint Persentations',  
    '.mp3': 'Audio',  
    '.wav': 'Audio',  
    '.mp4': 'Video',  
    '.avi': 'Video',  
    '.exe': 'Executable Files',  
    '.py': 'Python Files',  
    '.cpp': 'C++ Files',  
    '.c': 'C Files',  
    '.java': 'Java Files',  
    '.html': 'HTML Files',  
    '.css': 'CSS Files',  
    '.js': 'Javascript Files',  
    '.zip': 'Zip_Files'  
}  
  
# Create the destination folders if they don't already exist  
for folder_name in set(extension_map.values()):  
    os.makedirs(os.path.join(dest_dir, folder_name), exist_ok=True)  
  
# Loop through each file in the source directory and  
# Move it to the appropriate folder in the destination directory  
for filename in os.listdir(source_dir):  
  
    # Get the file extension in lowercase  
    file_ext = os.path.splitext(filename)[-1].lower()  
  
    # Check if the file extension is in the extension_map dictionary  
    if file_ext in extension_map:  
  
        # Create the full path to the source file  
        src_path = os.path.join(source_dir, filename)  
  
        # Create the full path to the destination file  
        dest_path = os.path.join(dest_dir, extension_map[file_ext], filename)  
  
        # Move the file to the appropriate folder in the destination directory  
        shutil.move(src_path, dest_path)

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# def main():
#     MY_ADDRESS = '***********'  # Specify sender's email address here
#     PASSWORD = '************'  # Specify sender's email password here
#     RECIPIENT_EMAIL = '22cs007@charusat.edu.in'  # Specify recipient's email address here
    
#     # set up the SMTP server
#     s = smtplib.SMTP(host='smtp.gmail.com', port=587)
#     s.starttls()
#     s.login(MY_ADDRESS, PASSWORD)
 
#     message = """
#     Dear Recipient,

#     This is the message content that you want to send. You can type your message here.

#     Sincerely,
#     Sujal vekariya.
#     """

#     msg = MIMEMultipart()  # create a message
#     # setup the parameters of the message
#     msg['From'] = MY_ADDRESS
#     msg['To'] = RECIPIENT_EMAIL
#     msg['Subject'] = 'Your Subject Here'  # Specify email subject here
#     # add in the message body
#     msg.attach(MIMEText(message, 'plain'))
#     # send the message via the server set up earlier.
#     s.send_message(msg)
        
#     # Terminate the SMTP session and close the connection
#     s.quit()

# if __name__ == '__main__':
#     main()
