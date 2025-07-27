// static/js/main.js - Main JavaScript file for the application
// Location: static/js directory

document.addEventListener('DOMContentLoaded', function() {
    // Chat functionality
    const messageForm = document.querySelector('.message-form');
    const messageInput = document.querySelector('.message-input');
    const chatMessages = document.querySelector('.chat-messages');

    if (messageForm && messageInput && chatMessages) {
        messageForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const message = messageInput.value.trim();
            if (message) {
                addUserMessage(message);
                messageInput.value = '';
                
                // Simulate AI response after a short delay
                setTimeout(() => {
                    addAIMessage('Thank you for your message! I\'m processing your request.');
                }, 1000);
            }
        });
    }

    // Function to add user message
    function addUserMessage(text) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message user-message';
        
        const now = new Date();
        const timeString = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
        
        messageDiv.innerHTML = `
            <div class="message-content">
                <p>${text}</p>
            </div>
            <div class="message-time">${timeString}</div>
        `;
        
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }

    // Function to add AI message
    function addAIMessage(text) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message ai-message';
        
        const now = new Date();
        const timeString = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
        
        messageDiv.innerHTML = `
            <div class="message-content">
                <p>${text}</p>
            </div>
            <div class="message-time">${timeString}</div>
        `;
        
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }

    // Function to scroll to bottom of chat
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Contact form handling
    const contactForm = document.querySelector('.contact-form form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(contactForm);
            const name = formData.get('name');
            const email = formData.get('email');
            const message = formData.get('message');
            
            if (name && email && message) {
                // Simulate form submission
                alert('Thank you for your message! We\'ll get back to you soon.');
                contactForm.reset();
            } else {
                alert('Please fill in all fields.');
            }
        });
    }

    // Sidebar navigation highlighting
    const navItems = document.querySelectorAll('.nav-item');
    const currentPath = window.location.pathname;
    
    navItems.forEach(item => {
        if (item.getAttribute('href') === currentPath) {
            item.style.backgroundColor = '#f8f9fa';
            item.style.borderLeftColor = '#667eea';
            item.style.color = '#667eea';
        }
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading animation for buttons
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (!this.classList.contains('loading')) {
                this.classList.add('loading');
                this.style.opacity = '0.7';
                
                setTimeout(() => {
                    this.classList.remove('loading');
                    this.style.opacity = '1';
                }, 1000);
            }
        });
    });
}); 