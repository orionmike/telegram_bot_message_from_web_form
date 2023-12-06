const form_message = document.querySelector('[class="form-message"]');
const message_block = document.querySelector('[class="block-result-message"]');
const login_url = '/api/message/send'

form_message.addEventListener('submit', send_form_message);

async function send_form_message(e) {
    e.preventDefault();

    const message = document.getElementById('bot-message').value;
    data = {}
    data["message"] = message

    let response = await fetch(login_url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    })

    if (response.ok) {
        let json = await response.json()
        // console.log(json)
        message_block.innerHTML = '<div id="result-message" class="text-success" style="margin-top: 20px;">message sended: ok</div>';
    } else {
        console.log(await response.text())
        message_block.innerHTML = '<div id="result-message" class="text-success" style="margin-top: 20px;">error</div>';
    }
    form_message.style.display = 'none';
}