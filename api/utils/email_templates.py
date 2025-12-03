from datetime import datetime

def get_subscription_email_template(subscriber_email):
    """
    Generate HTML email template for new subscription notifications
    
    Args:
        subscriber_email (str): Email address of the new subscriber
        
    Returns:
        tuple: (subject, text_content, html_content)
    """
    
    subject = '🔔 New Newsletter Subscription - Diginext'
    
    # Plain text version (fallback)
    text_content = f'''
New Newsletter Subscription

A new user has subscribed to your newsletter!

Subscriber Email: {subscriber_email}
Subscription Date: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}

---
Diginext Subscription System
    '''
    
    # HTML version - Simple & Clean Design
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Subscription</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f4f8;">
    <table role="presentation" style="width: 100%; border-collapse: collapse;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table role="presentation" style="width: 600px; border-collapse: collapse; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 50px 40px; text-align: center;">
                            <div style="background-color: rgba(255, 255, 255, 0.2); width: 80px; height: 80px; border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center;">
                                <span style="font-size: 40px;">📧</span>
                            </div>
                            <h1 style="margin: 0; color: #ffffff; font-size: 32px; font-weight: 700; letter-spacing: -0.5px;">
                                New Subscriber!
                            </h1>
                            <p style="margin: 12px 0 0 0; color: #e0e7ff; font-size: 16px; font-weight: 400;">
                                Your newsletter just got a new member
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Content -->
                    <tr>
                        <td style="padding: 50px 40px;">
                            <p style="margin: 0 0 30px 0; color: #4a5568; font-size: 17px; line-height: 1.6;">
                                Great news! Someone has joined your mailing list.
                            </p>
                            
                            <!-- Subscriber Info Box -->
                            <table role="presentation" style="width: 100%; border-collapse: collapse; background: linear-gradient(135deg, #f6f8fb 0%, #f0f4f8 100%); border-radius: 12px; margin: 25px 0; border: 2px solid #e2e8f0;">
                                <tr>
                                    <td style="padding: 35px;">
                                        <div style="text-align: center; margin-bottom: 20px;">
                                            <span style="display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 8px 20px; border-radius: 20px; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                                                Subscriber Details
                                            </span>
                                        </div>
                                        <table role="presentation" style="width: 100%; border-collapse: collapse;">
                                            <tr>
                                                <td style="padding: 20px; text-align: center; background-color: white; border-radius: 8px;">
                                                    <div style="color: #718096; font-size: 13px; font-weight: 600; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 0.5px;">
                                                        Email Address
                                                    </div>
                                                    <div style="color: #667eea; font-size: 20px; font-weight: 700; word-break: break-all;">
                                                        {subscriber_email}
                                                    </div>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Date Info -->
                            <div style="background-color: #fefcff; border-left: 4px solid #667eea; padding: 20px; border-radius: 6px; margin: 25px 0;">
                                <span style="color: #718096; font-size: 14px; font-weight: 600;">📅 Subscribed on:</span>
                                <span style="color: #2d3748; font-size: 15px; font-weight: 500; margin-left: 10px;">
                                    {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
                                </span>
                            </div>
                            
                            <!-- Action Button -->
                            <table role="presentation" style="width: 100%; border-collapse: collapse; margin: 40px 0 20px 0;">
                                <tr>
                                    <td align="center">
                                        <a href="mailto:{subscriber_email}" style="display: inline-block; padding: 16px 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #ffffff; text-decoration: none; border-radius: 8px; font-weight: 600; font-size: 16px; box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4); transition: all 0.3s;">
                                            📬 Contact Subscriber
                                        </a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #fafbfc; padding: 35px 40px; text-align: center; border-top: 1px solid #e2e8f0;">
                            <p style="margin: 0 0 8px 0; color: #2d3748; font-size: 17px; font-weight: 600;">
                                Diginext
                            </p>
                            <p style="margin: 0 0 15px 0; color: #718096; font-size: 14px;">
                                Newsletter Subscription System
                            </p>
                            <p style="margin: 0; color: #a0aec0; font-size: 12px;">
                                © {datetime.now().year} Diginext. All rights reserved.
                            </p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
    '''
    
    return subject, text_content, html_content


def get_subscription_confirmation_email_template(subscriber_email):
    """
    Generate confirmation email template for the subscriber
    
    Args:
        subscriber_email (str): Email address of the new subscriber
        
    Returns:
        tuple: (subject, text_content, html_content)
    """
    
    subject = '✅ Welcome to Diginext Newsletter!'
    
    # Plain text version
    text_content = f'''
Welcome to Diginext Newsletter!

Thank you for subscribing to our newsletter!

We're excited to have you as part of our community. You'll receive updates, insights, and exclusive content directly to your inbox.

Stay tuned for great content!

Best regards,
The Diginext Team

---
If you didn't subscribe to this newsletter, please ignore this email.
    '''
    
    # HTML version - Confirmation Design
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Diginext</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f4f8;">
    <table role="presentation" style="width: 100%; border-collapse: collapse;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table role="presentation" style="width: 600px; border-collapse: collapse; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 50px 40px; text-align: center;">
                            <div style="background-color: rgba(255, 255, 255, 0.2); width: 90px; height: 90px; border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center;">
                                <span style="font-size: 45px;">✅</span>
                            </div>
                            <h1 style="margin: 0; color: #ffffff; font-size: 36px; font-weight: 700; letter-spacing: -0.5px;">
                                You're Subscribed!
                            </h1>
                            <p style="margin: 15px 0 0 0; color: #e0e7ff; font-size: 18px; font-weight: 400;">
                                Welcome to the Diginext community
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Content -->
                    <tr>
                        <td style="padding: 50px 40px;">
                            <p style="margin: 0 0 25px 0; color: #2d3748; font-size: 18px; line-height: 1.7; text-align: center;">
                                🎉 <strong>Thank you for subscribing!</strong>
                            </p>
                            
                            <p style="margin: 0 0 30px 0; color: #4a5568; font-size: 16px; line-height: 1.7;">
                                We're thrilled to have you join our newsletter community. You'll receive:
                            </p>
                            
                            <!-- Benefits List -->
                            <table role="presentation" style="width: 100%; border-collapse: collapse; margin: 30px 0;">
                                <tr>
                                    <td style="padding: 20px; background: linear-gradient(135deg, #f6f8fb 0%, #f0f4f8 100%); border-radius: 10px; margin-bottom: 15px;">
                                        <div style="color: #667eea; font-size: 24px; margin-bottom: 10px;">📰</div>
                                        <div style="color: #2d3748; font-size: 16px; font-weight: 600; margin-bottom: 5px;">Latest Updates</div>
                                        <div style="color: #718096; font-size: 14px; line-height: 1.6;">Stay informed about our newest products, services, and company news.</div>
                                    </td>
                                </tr>
                                <tr><td style="height: 15px;"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background: linear-gradient(135deg, #f6f8fb 0%, #f0f4f8 100%); border-radius: 10px; margin-bottom: 15px;">
                                        <div style="color: #667eea; font-size: 24px; margin-bottom: 10px;">💡</div>
                                        <div style="color: #2d3748; font-size: 16px; font-weight: 600; margin-bottom: 5px;">Exclusive Insights</div>
                                        <div style="color: #718096; font-size: 14px; line-height: 1.6;">Get expert tips, industry trends, and valuable content delivered to your inbox.</div>
                                    </td>
                                </tr>
                                <tr><td style="height: 15px;"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background: linear-gradient(135deg, #f6f8fb 0%, #f0f4f8 100%); border-radius: 10px;">
                                        <div style="color: #667eea; font-size: 24px; margin-bottom: 10px;">🎁</div>
                                        <div style="color: #2d3748; font-size: 16px; font-weight: 600; margin-bottom: 5px;">Special Offers</div>
                                        <div style="color: #718096; font-size: 14px; line-height: 1.6;">Be the first to know about exclusive promotions and opportunities.</div>
                                    </td>
                                </tr>
                            </table>
                            
                            <div style="background-color: #fefcff; border: 2px dashed #667eea; padding: 25px; border-radius: 10px; margin: 35px 0; text-align: center;">
                                <p style="margin: 0; color: #4a5568; font-size: 15px; line-height: 1.7;">
                                    <strong style="color: #667eea;">📧 Subscribed Email:</strong><br>
                                    <span style="color: #2d3748; font-size: 17px; font-weight: 600;">{subscriber_email}</span>
                                </p>
                            </div>
                            
                            <p style="margin: 30px 0 0 0; color: #718096; font-size: 14px; line-height: 1.7; text-align: center;">
                                We respect your privacy and will never share your information.<br>
                                You can unsubscribe at any time.
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #fafbfc; padding: 35px 40px; text-align: center; border-top: 1px solid #e2e8f0;">
                            <p style="margin: 0 0 8px 0; color: #2d3748; font-size: 17px; font-weight: 600;">
                                Diginext
                            </p>
                            <p style="margin: 0 0 15px 0; color: #718096; font-size: 14px;">
                                hello@diginext.ae
                            </p>
                            <p style="margin: 0; color: #a0aec0; font-size: 12px;">
                                © {datetime.now().year} Diginext. All rights reserved.
                            </p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
    '''
    
    return subject, text_content, html_content


def get_lead_confirmation_email_template(fullname, solution):
    """
    Generate confirmation email template for the lead sender
    
    Args:
        fullname (str): Full name of the lead
        solution (str): Solution they're interested in
        
    Returns:
        tuple: (subject, text_content, html_content)
    """
    
    subject = '✅ We Received Your Inquiry - Diginext'
    
    # Plain text version
    text_content = f'''
Thank You for Contacting Diginext!

Hi {fullname},

Thank you for reaching out to us regarding {solution}.

We've received your inquiry and our team will review it shortly. One of our specialists will get back to you within 24-48 hours.

In the meantime, feel free to explore our website or reach out to us at hello@diginext.ae if you have any urgent questions.

Best regards,
The Diginext Team

---
This is an automated confirmation. Please do not reply to this email.
    '''
    
    # HTML version - Dark Professional Confirmation
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inquiry Received</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f1419;">
    <table role="presentation" style="width: 100%; border-collapse: collapse;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table role="presentation" style="width: 600px; border-collapse: collapse; background-color: #1a1f2e; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 50px 40px; text-align: center;">
                            <div style="background-color: rgba(255, 255, 255, 0.2); width: 90px; height: 90px; border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center;">
                                <span style="font-size: 45px;">✅</span>
                            </div>
                            <h1 style="margin: 0; color: #ffffff; font-size: 36px; font-weight: 800; letter-spacing: -1px;">
                                MESSAGE RECEIVED!
                            </h1>
                            <p style="margin: 15px 0 0 0; color: #d1fae5; font-size: 18px; font-weight: 500;">
                                We'll be in touch soon
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Content -->
                    <tr>
                        <td style="padding: 50px 40px;">
                            <p style="margin: 0 0 10px 0; color: #ffffff; font-size: 22px; font-weight: 700;">
                                Hi {fullname},
                            </p>
                            
                            <p style="margin: 0 0 30px 0; color: #9ca3af; font-size: 16px; line-height: 1.8;">
                                Thank you for reaching out to Diginext! We're excited about the opportunity to work with you.
                            </p>
                            
                            <!-- Inquiry Details -->
                            <div style="background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%); border-radius: 12px; padding: 30px; border: 1px solid #374151; margin: 30px 0;">
                                <div style="color: #10b981; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 15px;">
                                    📋 Your Inquiry Details
                                </div>
                                <div style="color: #6b7280; font-size: 14px; margin-bottom: 8px;">
                                    Interested in:
                                </div>
                                <div style="color: #ffffff; font-size: 20px; font-weight: 700;">
                                    {solution}
                                </div>
                            </div>
                            
                            <!-- What's Next Section -->
                            <div style="background-color: #0f172a; border-radius: 12px; padding: 30px; border-left: 4px solid #10b981; margin: 30px 0;">
                                <div style="color: #10b981; font-size: 16px; font-weight: 700; margin-bottom: 20px;">
                                    ⏭️ What Happens Next?
                                </div>
                                
                                <table role="presentation" style="width: 100%; border-collapse: collapse;">
                                    <tr>
                                        <td style="padding: 15px 0; border-bottom: 1px solid #1e293b;">
                                            <div style="color: #10b981; font-size: 24px; font-weight: 700; margin-bottom: 5px;">1</div>
                                            <div style="color: #e2e8f0; font-size: 15px; font-weight: 600; margin-bottom: 5px;">Review</div>
                                            <div style="color: #9ca3af; font-size: 14px;">Our team will carefully review your inquiry</div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 15px 0; border-bottom: 1px solid #1e293b;">
                                            <div style="color: #10b981; font-size: 24px; font-weight: 700; margin-bottom: 5px;">2</div>
                                            <div style="color: #e2e8f0; font-size: 15px; font-weight: 600; margin-bottom: 5px;">Connect</div>
                                            <div style="color: #9ca3af; font-size: 14px;">A specialist will reach out within 24-48 hours</div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 15px 0;">
                                            <div style="color: #10b981; font-size: 24px; font-weight: 700; margin-bottom: 5px;">3</div>
                                            <div style="color: #e2e8f0; font-size: 15px; font-weight: 600; margin-bottom: 5px;">Solutions</div>
                                            <div style="color: #9ca3af; font-size: 14px;">We'll discuss the best approach for your needs</div>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                            
                            <!-- Contact Info -->
                            <div style="background: linear-gradient(135deg, #FF6B6B 0%, #FFE66D 100%); border-radius: 12px; padding: 25px; margin: 30px 0; text-align: center;">
                                <div style="color: #1a202c; font-size: 15px; font-weight: 700; margin-bottom: 10px;">
                                    Need immediate assistance?
                                </div>
                                <a href="mailto:hello@diginext.ae" style="color: #1a202c; font-size: 18px; font-weight: 700; text-decoration: none;">
                                    📧 hello@diginext.ae
                                </a>
                            </div>
                            
                            <p style="margin: 30px 0 0 0; color: #6b7280; font-size: 14px; line-height: 1.7; text-align: center; font-style: italic;">
                                We're committed to providing you with exceptional service and innovative solutions.
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #0f172a; padding: 35px 40px; text-align: center; border-top: 1px solid #1e293b;">
                            <p style="margin: 0 0 8px 0; color: #e2e8f0; font-size: 18px; font-weight: 700;">
                                DIGINEXT
                            </p>
                            <p style="margin: 0 0 15px 0; color: #6b7280; font-size: 13px;">
                                Digital Solutions That Drive Results
                            </p>
                            <p style="margin: 0; color: #4b5563; font-size: 12px;">
                                © {datetime.now().year} Diginext. All rights reserved.
                            </p>
                            <p style="margin: 10px 0 0 0; color: #4b5563; font-size: 11px;">
                                This is an automated message. Please do not reply to this email.
                            </p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
    '''
    
    return subject, text_content, html_content


def get_lead_notification_email_template(fullname, email, phone_number, company_name, solution, message):
    """
    Generate HTML email template for new lead notifications
    
    Args:
        fullname (str): Full name of the lead
        email (str): Email address of the lead
        phone_number (str): Phone number of the lead
        company_name (str): Company name of the lead
        solution (str): Solution they're interested in
        message (str): Message from the lead
        
    Returns:
        tuple: (subject, text_content, html_content)
    """
    
    subject = '🎯 New Business Lead - Diginext'
    
    # Plain text version (fallback)
    text_content = f'''
New Business Lead Received

A potential client has submitted an inquiry!

Contact Details:
----------------
Name: {fullname}
Company: {company_name}
Email: {email}
Phone: {phone_number}
Interested In: {solution}

Message:
--------
{message}

Received: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}

---
Diginext Lead Management System
    '''
    
    # HTML version - Professional Business Design
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Lead</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f1419;">
    <table role="presentation" style="width: 100%; border-collapse: collapse;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table role="presentation" style="width: 650px; border-collapse: collapse; background-color: #1a1f2e; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #FF6B6B 0%, #FFE66D 100%); padding: 0; position: relative;">
                            <div style="padding: 45px 40px; background: linear-gradient(135deg, rgba(255, 107, 107, 0.95) 0%, rgba(255, 230, 109, 0.95) 100%);">
                                <table role="presentation" style="width: 100%;">
                                    <tr>
                                        <td style="vertical-align: middle;">
                                            <div style="display: inline-block; background-color: rgba(255, 255, 255, 0.25); padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                                                <span style="font-size: 36px;">🎯</span>
                                            </div>
                                            <h1 style="margin: 0; color: #ffffff; font-size: 34px; font-weight: 800; letter-spacing: -1px;">
                                                NEW LEAD ALERT
                                            </h1>
                                            <p style="margin: 10px 0 0 0; color: #fff8dc; font-size: 17px; font-weight: 500;">
                                                A potential client is ready to connect
                                            </p>
                                        </td>
                                        <td style="text-align: right; vertical-align: top;">
                                            <div style="background-color: rgba(255, 255, 255, 0.3); padding: 10px 18px; border-radius: 8px; display: inline-block;">
                                                <span style="color: #ffffff; font-size: 13px; font-weight: 700; text-transform: uppercase;">Priority</span>
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Content -->
                    <tr>
                        <td style="padding: 45px 40px;">
                            
                            <!-- Client Info Grid -->
                            <table role="presentation" style="width: 100%; border-collapse: collapse; margin-bottom: 30px;">
                                <tr>
                                    <!-- Left Column -->
                                    <td style="width: 50%; padding-right: 15px; vertical-align: top;">
                                        <div style="background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%); border-radius: 12px; padding: 25px; border: 1px solid #374151; height: 100%;">
                                            <div style="color: #FFE66D; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;">
                                                👤 Contact Person
                                            </div>
                                            <div style="color: #ffffff; font-size: 22px; font-weight: 700; margin-bottom: 18px; line-height: 1.3;">
                                                {fullname}
                                            </div>
                                            
                                            <div style="margin-bottom: 15px;">
                                                <div style="color: #9ca3af; font-size: 12px; margin-bottom: 5px;">📧 Email</div>
                                                <a href="mailto:{email}" style="color: #60a5fa; font-size: 15px; text-decoration: none; word-break: break-all;">
                                                    {email}
                                                </a>
                                            </div>
                                            
                                            <div>
                                                <div style="color: #9ca3af; font-size: 12px; margin-bottom: 5px;">📱 Phone</div>
                                                <a href="tel:{phone_number}" style="color: #60a5fa; font-size: 15px; text-decoration: none;">
                                                    {phone_number}
                                                </a>
                                            </div>
                                        </div>
                                    </td>
                                    
                                    <!-- Right Column -->
                                    <td style="width: 50%; padding-left: 15px; vertical-align: top;">
                                        <div style="background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%); border-radius: 12px; padding: 25px; border: 1px solid #374151; margin-bottom: 15px;">
                                            <div style="color: #FFE66D; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;">
                                                🏢 Company
                                            </div>
                                            <div style="color: #ffffff; font-size: 20px; font-weight: 700; line-height: 1.3;">
                                                {company_name}
                                            </div>
                                        </div>
                                        
                                        <div style="background: linear-gradient(135deg, #FF6B6B 0%, #FFE66D 100%); border-radius: 12px; padding: 25px;">
                                            <div style="color: #1a202c; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;">
                                                💡 Interested In
                                            </div>
                                            <div style="color: #1a202c; font-size: 18px; font-weight: 700; line-height: 1.3;">
                                                {solution}
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Message Box -->
                            <div style="background-color: #1e293b; border-radius: 12px; padding: 30px; border-left: 4px solid #FFE66D; margin-bottom: 30px;">
                                <div style="color: #FFE66D; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 15px;">
                                    💬 Their Message
                                </div>
                                <p style="margin: 0; color: #e2e8f0; font-size: 16px; line-height: 1.8; white-space: pre-wrap;">
{message}
                                </p>
                            </div>
                            
                            <!-- Timestamp -->
                            <div style="background-color: #0f172a; border-radius: 8px; padding: 18px; margin-bottom: 35px; border: 1px solid #1e293b;">
                                <span style="color: #9ca3af; font-size: 13px;">
                                    ⏰ Received: <span style="color: #e2e8f0; font-weight: 600;">{datetime.now().strftime('%B %d, %Y at %I:%M %p')}</span>
                                </span>
                            </div>
                            
                            <!-- Action Buttons -->
                            <table role="presentation" style="width: 100%; border-collapse: collapse;">
                                <tr>
                                    <td style="padding-right: 10px; width: 50%;">
                                        <a href="mailto:{email}?subject=Re: {solution} Inquiry&body=Hi {fullname}," style="display: block; padding: 18px 25px; background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%); color: #ffffff; text-decoration: none; border-radius: 10px; font-weight: 700; font-size: 15px; text-align: center; box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);">
                                            📧 Send Email
                                        </a>
                                    </td>
                                    <td style="padding-left: 10px; width: 50%;">
                                        <a href="tel:{phone_number}" style="display: block; padding: 18px 25px; background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: #ffffff; text-decoration: none; border-radius: 10px; font-weight: 700; font-size: 15px; text-align: center; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);">
                                            📞 Call Now
                                        </a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 30px 0 0 0; color: #6b7280; font-size: 14px; line-height: 1.6; text-align: center; font-style: italic;">
                                ⚡ Quick response increases conversion by 391%
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #0f172a; padding: 35px 40px; text-align: center; border-top: 1px solid #1e293b;">
                            <p style="margin: 0 0 8px 0; color: #e2e8f0; font-size: 18px; font-weight: 700;">
                                DIGINEXT
                            </p>
                            <p style="margin: 0 0 15px 0; color: #6b7280; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">
                                Lead Management System
                            </p>
                            <p style="margin: 0; color: #4b5563; font-size: 12px;">
                                © {datetime.now().year} Diginext. All rights reserved.
                            </p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
    '''
    
    return subject, text_content, html_content
