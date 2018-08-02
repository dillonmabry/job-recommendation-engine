export default function ValidateEmail(email) {
    // RFC 2822 email regex
    const emailRegex = new RegExp(`[a-z0-9!#$%&*+/=?^_{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?`)
    return email.match(emailRegex)
}