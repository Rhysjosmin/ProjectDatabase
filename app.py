import csv
import json
from datetime import date, datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
class CSVEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('data.csv'):
            convert_csv_to_json()

def convert_csv_to_json():
    # Read the CSV file
    with open('data.csv', 'r') as file:
        csv_data = csv.reader(file)
        next(csv_data)  # Skip the header row
        manylinksMain='https://rhysjosmin.github.io/ManyLinks/'
        projects = []
        Files=os.listdir('Media/')
      
        # Process each row in the CSV file
        for row in csv_data:
            name = row[0]
            date_created = row[1]
            date_end = row[2]
            src = row[3]
            Image = row[4]
            Vertical=row[5]
        
            
            if 'manylinks' in src:
                src=manylinksMain + src.split('+')[1].replace('<>',',')
            if Image == 'Image' or Image == 'imgName':
                print('No Image : ' ,end='')
                print(name)
            elif Image not in Files:
                print('Image Not Found : ' ,end='')
                print(name)
            try:
                Start = f"{date_created.split(' ')[1]}-{datetime.strptime(date_created.split(' ')[0], '%B').month}-{date_created.split(' ')[2]}"
            except:
                print('No Date : ' ,end='')
                print(name )
                Start = '1-1-2019'
            # Create a project dictionary
            project = {
                "Name": name,
                "Date Created": date_created,
                "src": src,
                "Type": "",
                "Medium": "",
                "Description": "",
                "Tags": [],
                "Timeline": {
                    "Start": Start,
                    "End": date_end
                },
                "Status": "",
                "Manager": "Rhys Josmin",
                "Risks": "",
                "Notes": "",
                "Project Customer": [],
                "Img": Image,
                "Sub Projects": [],
            "VerticalPosition":Vertical
            }

            # Add the project to the list
            projects.append(project)
        # Create the JSON data
        json_data = {
            "Date-Created": "25 Jun 2023",
            "Modified": date.today().strftime("%d %B %Y"),
            "Projects": projects
        }

        # Convert the JSON data to a string
        json_string = json.dumps(json_data, indent=2)

        # Write the JSON data to a file
        with open('data.json', 'w') as json_file:
            json_file.write(json_string)

       
       
        print("Conversion completed successfully!")

# Create an observer and event handler
event_handler = CSVEventHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=False)

# Start the observer
observer.start()

try:
    while True:
        # Keep the script running
        pass
except KeyboardInterrupt:
    # Stop the observer when Ctrl+C is pressed
    observer.stop()

# Wait until the observer thread completes its execution
observer.join()
