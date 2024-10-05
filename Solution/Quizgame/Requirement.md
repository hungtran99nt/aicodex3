# Functional Requirements for Quiz Game

# High-Level Requirements Table

## Functional Requirements

| Areas               | High-Level Requirement | Priority |
|---------------------|--------------------------------|----------|
| User Management     | User Registration and Login    | High     |
| User Management     | User Profiles                  | High     |
| Quiz Creation       | Quiz Builder                   | High     |
| Quiz Creation       | Question Bank                  | Medium   |
| Quiz Creation       | Media Support                  | Medium   |
| Quiz Participation  | Live Quizzes                   | High     |
| Quiz Participation  | Self-Paced Quizzes             | Medium   |
| Quiz Participation  | Real-Time Feedback             | High     |
| Scoring and Leaderboards | Scoring System            | High     |
| Scoring and Leaderboards | Leaderboards              | Medium   |
| Social Features     | Sharing                        | Medium   |
| Social Features     | Comments and Ratings           | Medium   |
| Administration      | Admin Dashboard                | High     |
| Administration      | Analytics                      | Medium   |

## Non-Functional Requirements

| Areas               | Name of High-Level Requirement | Priority |
|---------------------|--------------------------------|----------|
| Security and Compliance | Data Protection            | High     |
| Security and Compliance | User Privacy               | High     |

## 1. User Management
- **User Registration:**
  - Users should be able to register using email, username, and password.
  - Users should be able to register using social media accounts (e.g., Google, Facebook).
  - **Validation:** Ensure email format is correct and password meets security criteria (e.g., minimum length, special characters).
  - **Prototype:** Registration form with fields for email, username, password, and social media login buttons.
- **User Login:**
  - Users should be able to log in using email and password.
  - Users should be able to log in using social media accounts.
  - **Validation:** Ensure email and password match registered credentials.
  - **Prototype:** Login form with fields for email, password, and social media login buttons.
- **Password Management:**
  - Users should be able to reset their password via email.
  - Users should be able to change their password from their profile settings.
  - **Validation:** Ensure new password meets security criteria.
  - **Prototype:** Password reset form and change password form.
- **User Profiles:**
  - Users should be able to view and edit their profile information.
  - Users should be able to upload a profile picture.
  - Users should be able to view their quiz history and achievements.
  - **Validation:** Ensure profile updates are saved correctly.
  - **Prototype:** Profile page with editable fields and upload button for profile picture.

## 2. Quiz Creation
- **Quiz Builder:**
  - Users should be able to create a new quiz by providing a title and description.
  - Users should be able to add multiple types of questions (multiple choice, true/false, short answer).
  - Users should be able to set a time limit for each question.
  - Users should be able to add images, videos, and audio to questions.
  - **Validation:** Ensure all required fields are filled and media files are in supported formats.
  - **Prototype:** Quiz creation form with fields for title, description, question types, time limit, and media upload.
- **Question Bank:**
  - Users should be able to save questions to a personal question bank.
  - Users should be able to categorize and tag questions for easy retrieval.
  - Users should be able to import questions from a file (e.g., CSV, JSON).
  - **Validation:** Ensure imported files are in correct format and questions are saved correctly.
  - **Prototype:** Question bank interface with options to add, categorize, tag, and import questions.

## 3. Quiz Participation
- **Live Quizzes:**
  - Users should be able to join live quizzes using a unique code.
  - Hosts should be able to start, pause, and end the quiz.
  - Participants should see questions and answer choices in real-time.
  - **Validation:** Ensure real-time synchronization and correct display of questions and answers.
  - **Prototype:** Live quiz interface with fields for joining code and real-time question display.
- **Self-Paced Quizzes:**
  - Users should be able to take quizzes at their own pace.
  - Users should receive immediate feedback on their answers.
  - **Validation:** Ensure correct feedback is provided for each answer.
  - **Prototype:** Self-paced quiz interface with immediate feedback display.
- **Real-Time Feedback:**
  - Participants should receive real-time feedback on their answers during live quizzes.
  - Correct answers and explanations should be displayed after each question.
  - **Validation:** Ensure feedback is accurate and timely.
  - **Prototype:** Feedback display interface for live quizzes.

## 4. Scoring and Leaderboards
- **Scoring System:**
  - Points should be awarded based on correct answers and response time.
  - Quiz creators should be able to customize scoring rules.
  - **Validation:** Ensure scoring is calculated correctly based on rules.
  - **Prototype:** Scoring settings interface for quiz creators.
- **Leaderboards:**
  - Leaderboards should display the top participants for each quiz.
  - Weekly, monthly, and all-time leaderboards should be available.
  - Users should be able to view their ranking on the leaderboard.
  - **Validation:** Ensure leaderboards are updated correctly and rankings are accurate.
  - **Prototype:** Leaderboard display interface.

## 5. Social Features
- **Sharing:**
  - Users should be able to share quizzes on social media platforms.
  - Unique links should be generated for sharing quizzes.
  - **Validation:** Ensure links are generated correctly and are shareable.
  - **Prototype:** Sharing options interface with social media buttons and unique link generation.
- **Comments and Ratings:**
  - Users should be able to comment on and rate quizzes.
  - Moderation tools should be available to manage inappropriate content.
  - **Validation:** Ensure comments and ratings are saved correctly and moderation tools are functional.
  - **Prototype:** Comments and ratings interface with moderation options.

## 6. Administration
- **Admin Dashboard:**
  - Admins should be able to manage users, quizzes, and reported content.
  - Admins should have access to analytics on user engagement and quiz performance.
  - **Validation:** Ensure admin actions are logged and analytics data is accurate.
  - **Prototype:** Admin dashboard interface with management and analytics options.
- **Analytics:**
  - Detailed analytics should be provided on quiz performance and user engagement.
  - Analytics data should be exportable for further analysis.
  - **Validation:** Ensure analytics data is accurate and export functionality works correctly.
  - **Prototype:** Analytics display and export interface.

## 7. Security and Compliance
- **Data Protection:**
  - The system should comply with data protection regulations (e.g., GDPR).
  - Sensitive data should be encrypted.
  - **Validation:** Ensure data protection measures are in place and encryption is functional.
  - **Prototype:** Data protection settings interface.
- **User Privacy:**
  - Users should be able to control the visibility of their quizzes and profile information.
  - Privacy settings should be available for user profiles and quizzes.
  - **Validation:** Ensure privacy settings are saved correctly and applied.
  - **Prototype:** Privacy settings interface for user profiles and quizzes.