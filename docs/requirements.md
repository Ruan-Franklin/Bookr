# Bookr Requirements Document

## 1. Project Overview

Bookr is a modern full-stack booking and scheduling platform for service-based businesses. The system is designed to help clients book appointments with professionals, while allowing service providers to manage services, schedules, and customer relationships in one place.

The project is intended for businesses such as barbershops, clinics, gyms, and sports courts, where appointments and service availability are central to daily operations.

## 2. Goals

The main goals of Bookr are to:

- simplify the scheduling process for customers and professionals
- centralize service listings and appointment management
- improve operational efficiency for service providers
- allow users to manage personal profiles and authentication securely
- create a scalable foundation for future features such as payments, reminders, and dashboards

## 3. Scope

### In scope

- user registration and login
- user and professional profiles
- service catalog management
- appointment creation and tracking
- reviews and ratings
- service availability and scheduling logic
- role-based interactions between customers and professionals

### Out of scope for initial version

- online payment processing
- automated reminders and notifications
- complex calendar integrations
- admin analytics dashboards
- multi-location management
- mobile app development

## 4. Users and Roles

### 4.1 User
A User represents a customer or registered platform account. A user can:

- create and manage a personal profile
- log in securely
- search for and view services
- book appointments
- review services or professionals

### 4.2 Professional
A Professional represents a service provider or business member. A professional can:

- create and update a professional profile
- define specialties and experience
- manage services offered
- manage appointments
- review their booking activity and service reputation

## 5. Functional Requirements

### FR1. User Registration and Authentication
The system must allow a user to register with personal information such as name, email, phone number, and password.

The system must:

- validate required fields
- store credentials securely
- allow login with the registered email and password
- support password hashing or protected storage

### FR2. User Profile Management
Users must be able to manage their own profile, including:

- first name and last name
- email address
- phone number
- profile picture
- document number if required by business rules

### FR3. Professional Profile Management
Professionals must have a profile containing:

- name
- biography
- specialty
- rating or reputation information
- total reviews

### FR4. Service Management
Each service must include:

- name
- description
- duration in minutes
- price
- image

The system must allow a professional to define and manage the services they offer.

### FR5. Appointment Booking
Users must be able to create appointments for a selected service and professional.

Each appointment must include:

- start time
- status
- associated user and professional
- associated service

The system should allow the status of an appointment to be tracked throughout its lifecycle, such as scheduled, confirmed, completed, or cancelled.

### FR6. Review and Rating
Users must be able to leave a review and rating for a professional or service after an appointment is completed or after a service interaction.

Each review must include:

- rating
- comment
- date or timestamp

### FR7. Base Entity and Audit Tracking
The system must include shared metadata via a base model, including:

- created at
- updated at
- deleted at
- created by
- changed by

This is important for traceability, auditing, and future administrative features.

## 6. Business Rules

- A user may have one or more appointment records.
- A professional may offer one or more services.
- Each appointment must be associated with exactly one user and one professional.
- A service must belong to a professional or service provider.
- A review may be linked to a user and a professional or service.
- Appointment status must be controlled by the system to prevent invalid transitions.
- A user cannot book a service if required profile information is missing.

## 7. Non-Functional Requirements

### NFR1. Usability
The platform should be intuitive for both clients and professionals, with clear flows for registration, browsing, booking, and review.

### NFR2. Security
The system must protect user credentials and sensitive profile data. Authentication must use secure practices, and access to personal or booking information must be properly restricted.

### NFR3. Performance
The system should respond quickly when listing services, loading profiles, and creating appointments. The booking flow should be efficient even as the number of users grows.

### NFR4. Scalability
The architecture should support growth in users, services, and appointments without requiring a complete redesign.

### NFR5. Maintainability
The domain model should remain modular and easy to extend, with clear separation between entities such as User, Professional, Service, Appointment, and Review.

## 8. Data Model Requirements

The project domain model includes the following entities:

- BaseModel: common attributes for all persistent entities
- User: personal data and authentication information
- Professional: specialty, bio, ratings, and reviews
- Service: service description, image, duration, and pricing
- Appointment: date, status, and service relationship
- Review: rating and comment data

This model should be implemented in a way that reflects the relationships identified in the class diagram.

## 9. Acceptance Criteria

### User flow
- A new user can register with valid credentials.
- A registered user can log in and update profile information.
- A user can view services and select one to book.
- A booking is created with a valid start time and status.

### Professional flow
- A professional can create or update their profile.
- A professional can add and manage services.
- A professional can view appointments linked to them.

### Review flow
- A user can create a review after using a service or professional.
- The review stores a rating and comment.

## 10. Summary

Bookr is a booking platform focused on service providers and their customers. The requirements defined here are based on the current business concept and domain model, and they establish the foundation for the application's data structure, workflows, and future implementation.
