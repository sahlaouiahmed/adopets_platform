# Adopets Platform

Welcome to Adopets Platform, your go-to solution for pet adoption! Our platform is designed to simplify and enhance the pet adoption process, making it easier for potential adopters to connect with pet owners. With Adopets, finding a loving home for every pet is just a few clicks away. Whether you're looking to adopt a pet or rehome a pet, our user-friendly interface and powerful search capabilities ensure a seamless experience for all users.

Additionally, explore our comprehensive library of pet care articles to provide the best for your new furry friends. Share your experiences, tips, and stories with other pet lovers in our community, and learn from others' experiences to make the journey of pet adoption even more rewarding.

Our website is deployed on Heroku. Check it out [here](https://adopetsplatform-4e35c86a8c8e.herokuapp.com/).



## Key Features

### Posting Pets
Easily post pets available for adoption on our platform. Provide detailed information, including photos, breed, age, and any special requirements. This helps potential adopters find the perfect match quickly and efficiently.

### Adoption Requests
Manage adoption requests seamlessly. Potential adopters can express their interest in adopting pets, and pet owners or shelters can review and respond to these requests. Our streamlined process ensures a smooth and transparent adoption experience for everyone involved.

### Research Using Filters
Find the ideal pet using our powerful search filters. Filter by species, breed, age, location, and more to narrow down your options and find pets that match your preferences. Our intuitive search functionality makes it easy to discover pets that are looking for a loving home.

### Account Creation
Sign up and create an account to start using the Adopets Platform. Whether you're a pet owner looking to rehome a pet or a potential adopter searching for a new companion, having an account allows you to manage your listings, adoption requests, and communication with ease.

### Articles of Pet Care
Explore our comprehensive library of articles on pet care. From feeding tips to grooming guides, our articles are designed to help pet owners provide the best care for their furry friends. Stay informed and ensure your pets are happy and healthy with our expert advice.

## Technologies Used

### Django
Django is the backbone of our platform. It’s a high-level Python web framework that encourages rapid development and clean, pragmatic design. Django takes care of much of the hassle of web development, allowing us to focus on writing your app without needing to reinvent the wheel. 

### PostgreSQL
We use PostgreSQL as our database management system. It’s a powerful, open-source object-relational database system that has earned a strong reputation for reliability, feature robustness, and performance.

### JavaScript
JavaScript powers the interactive elements of our site, ensuring a smooth and dynamic user experience. It's an essential technology for making our web pages more engaging and functional.

### HTML
HTML (HyperText Markup Language) is used to structure our web pages and content. It forms the skeleton of our web application, providing the essential building blocks for layout and organization.

### CSS
CSS (Cascading Style Sheets) is used for styling our HTML. It allows us to create a visually appealing interface that is both user-friendly and consistent across different browsers and devices.

### Bootstrap
Bootstrap is a popular front-end framework for developing responsive and mobile-first websites. It provides a collection of CSS and JavaScript components that make it easier to design beautiful and responsive web pages quickly.


## Website Functionalities

### User Registration and Login
- **Create an Account**: Users can sign up and create an account by providing their username, email, and password. This allows them to access additional features and manage their activity on the platform.
- **Login**: Registered users can log in to their accounts using their credentials, ensuring secure access to their personalized dashboard.

![User sign up and login interface](static/images/readme_photos/sign_up&login.png)

### Dashboard
- **User Dashboard**: Once logged in, users have access to a personalized dashboard where they can manage their posted pets, adoption requests, recieved adoption requests and their posted articles . The dashboard provides an overview of their activity on the platform.

![Home page ](static/images/readme_photos/home.png)


### Posting Pets
- **Add New Pet**: Users can post pets available for adoption by providing detailed information such as name, species, breed, age, gender, description, and photos. This helps potential adopters find the right pet easily.
- **Manage Posts**: Users can edit or delete their posted pets from their dashboard, ensuring that the information is always up-to-date.

![Postingpets](static/images/readme_photos/My-Posted-Pets.png)


### Adoption Requests
- **Submit Adoption Request**: Potential adopters can express their interest in adopting a pet by submitting an adoption request. They can write a message to the pet owner explaining why they are a good fit for the pet.
- **View Adoption Requests**: Pet owners can view the adoption requests they have received, including messages from potential adopters. This allows them to review and respond to requests directly from their dashboard.

![AdoptionRequests](static/images/readme_photos/AdoptionRequests.png)

### Pet Care Articles
- **Browse Articles**: Users can explore a comprehensive library of pet care articles covering various topics such as feeding, grooming, training, and health. The articles are designed to provide valuable information to pet owners and adopters.
- **Write and Share Articles**: Registered users can contribute to the community by writing and sharing their own articles. This allows them to share their experiences and tips with other pet lovers.

![AdoptionRequests](static/images/readme_photos/Petcaretips.png)

### Search and Filters
- **Search for Pets**: Users can search for pets based on various criteria such as species, breed, age, and location. This helps them find pets that match their preferences quickly and easily.
- **Filter Results**: Users can apply filters to narrow down their search results, making it easier to find the perfect pet.

![research filters](static/images/readme_photos/filters.png)






















## Entity-Relationship Diagrams (ERD)

Here are the ERDs for each model in the Adopets Platform database.

### User Model

#### Diagram:

Here's the Entity-Relationship Diagram (ERD) for the Django standard User model:

![User Model ERD](static/images/readme_photos/user_model.png)

#### Relationships:

- Groups: A many-to-many relationship with the Group model.

- Permissions: A many-to-many relationship with the Permission model.

### Pet Model 

#### Diagram:

![Pet Model ERD](static/images/readme_photos/pet_model.png)

#### Relationships
- User has a one-to-many relationship with Pet (a single user can post multiple pets).

### AdoptionRequest Model

#### Diagram:

![ AdoptionRequest Model ERD](static/images/readme_photos/AdoptionRequest_Model.png)

#### Relationships

- User has a one-to-many relationship with AdoptionRequest (a single user can make multiple adoption requests).

- Pet has a one-to-many relationship with AdoptionRequest (a single pet can have multiple adoption requests).

### Article Model

#### Diagram:

![ Article Model ERD](static/images/readme_photos/Article_Model.png)

#### Relationships

- User has a one-to-many relationship with Article (a single user can author multiple articles).



## Testing

To ensure the robustness and reliability of the Adopets Platform, we created comprehensive tests for all forms using Django's `unittest` framework. Here are the details of the tests we implemented:

### Form Tests

#### User Registration Form
We tested the `UserRegistrationForm` to ensure that users can successfully register with valid data, and that errors are properly handled when the data is invalid or incomplete.

#### Pet Form
We thoroughly tested the `PetForm` to confirm that users can add new pets with complete and valid information, including an image upload. We also verified that the form correctly handles missing or invalid data.

#### Adoption Request Form
The `AdoptionRequestForm` was tested to check that adoption requests can be submitted with a pre-filled message, and that the form is valid with both the default and custom initial messages.

#### Pet Search Form
We tested the `PetSearchForm` to ensure that users can search for pets based on various criteria such as species, breed, city, country, and posted by. The form was validated to work correctly with full, partial, and blank data.

#### Adoption Request Filter Form
We tested the `AdoptionRequestFilterForm` to confirm that users can filter adoption requests based on their status (pending, approved, rejected). The form was tested with valid, empty, and invalid data to ensure proper functionality.





















## Future Enhancements

We have some exciting plans for the Adopets Platform to make it even more user-friendly and comprehensive. Here are some of the enhancements we're considering:

1. **Mobile Application**: Developing a mobile app for both iOS and Android to make it even easier for users to access Adopets on the go.

2. **Advanced Search Filters**: Adding more advanced filters such as pet size, temperament, and special needs to help users find their perfect match more efficiently.

3. **Real-time Chat**: Implementing real-time chat functionality to allow instant communication between adopters and pet owners.

4. **Integration with Veterinary Services**: Partnering with local veterinary services to provide health check-ups and vaccinations for pets before adoption.

5. **Adoption Events**: Organizing and promoting local adoption events where users can meet pets in person and interact with other pet lovers.

6. **Pet Training Resources**: Providing a collection of resources and tutorials on pet training and behavior to help new pet owners.

7. **Donation and Sponsorship**: Enabling users to donate or sponsor pets, helping shelters and pet owners cover the costs of pet care.

8. **User Reviews and Ratings**: Allowing users to review and rate their adoption experiences, helping to build trust and improve the platform.

9. **Email Notifications**: Implementing email notifications to keep users informed about their pets, received adoption requests, and updates on adoption request statuses. These notifications will ensure users are always up-to-date with their activities on the platform.


These enhancements will help make the Adopets Platform an even more valuable resource for pet lovers and ensure that every pet finds a loving home.
