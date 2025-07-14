document.addEventListener('DOMContentLoaded', function() {
    // Toggle chatbot visibility
    const chatbotToggler = document.querySelector(".chatbot-toggler");
    const closeBtn = document.querySelector(".close-btn");
    const chatbot = document.querySelector(".chatbot");
    
    chatbotToggler.addEventListener("click", () => {
        document.body.classList.toggle("show-chatbot");
    });
    
    closeBtn.addEventListener("click", () => {
        document.body.classList.remove("show-chatbot");
    });

    // Send message function
    function sendMessage() {
        const userInput = $("#user-input");
        const msg = userInput.val().trim();
        
        if(!msg) return;
        
        // Add user message to chatbox
        $("#chatbox").append(
            `<li class="chat outgoing"><p>${msg}</p></li>`
        );
        
        // Clear input and scroll to bottom
        userInput.val("");
        scrollToBottom();
        
        // Show "Thinking..." message
        $("#chatbox").append(
            `<li class="chat incoming"><span class="material-symbols-outlined">smart_toy</span><p>Thinking...</p></li>`
        );
        scrollToBottom();
        
        // Send message to backend
        $.post("/get", {msg: msg})
            .done(function(data) {
                // Replace "Thinking..." with actual response
                $("#chatbox li:last-child p").text(data.response);
            })
            .fail(function() {
                $("#chatbox li:last-child p").text("Sorry, I'm having trouble connecting. Please try again later.");
                $("#chatbox li:last-child p").addClass("error");
            })
            .always(scrollToBottom);
    }
    
    // Scroll to bottom of chatbox
    function scrollToBottom() {
        $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);
    }
    
    // Event listeners
    $("#send-btn").click(sendMessage);
    $("#user-input").keypress(function(e){
        if(e.which == 13 && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
});