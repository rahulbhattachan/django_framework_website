from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        # Save contact to database
        contact = Contact(
            listing=listing, 
            listing_id=listing_id, 
            name=name, 
            email=email, 
            phone=phone, 
            message=message, 
            user_id=user_id
        )
        contact.save()

        # Send email notification
        try:
            # Email subject
            subject = f'Property Inquiry - {listing}'
            
            # Email body
            email_message = f"""
New property inquiry received:

Property: {listing}
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}

Please log into the admin panel for more details.
            """
            
            # Send email to realtor
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [realtor_email],  # Send to the realtor's email
                fail_silently=False
            )
            
            # Optional: Send confirmation email to client
            client_subject = f'Thank you for your inquiry about {listing}'
            client_message = f"""
Dear {name},

Thank you for your interest in {listing}. We have received your inquiry and will get back to you soon.

Your inquiry details:
- Property: {listing}
- Your message: {message}

Best regards,
BT Real Estate Team
            """
            
            send_mail(
                client_subject,
                client_message,
                settings.DEFAULT_FROM_EMAIL,
                [email],  # Send confirmation to client
                fail_silently=True  # Don't fail if client email fails
            )
            
            messages.success(request, 'Your request has been submitted. A realtor will get back to you soon!')
            
        except Exception as e:
            # Log the error for debugging
            print(f"Email sending failed: {str(e)}")
            messages.warning(request, 'Your inquiry has been saved, but there was an issue sending the email notification.')
        
        return redirect('/listings/'+listing_id)