document.addEventListener("DOMContentLoaded", () => {
    const fields = {
        email: document.querySelector("input[name='email']"),
        phone: document.querySelector("input[name='phone']"),
        username: document.querySelector("input[name='username']")
    };

    const regex = {
        email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        phone: /^(\d{10}|(\d{3} \d{3} \d{4})|(\d{5} \d{5}))$/,
        username: /^[a-zA-Z0-9_-]{2,}$/
    };

    function validateField(field, type) {
        const value = field.value.trim();
        const errorSpan = document.getElementById(`error-${type}`);

        if (!regex[type].test(value)) {
            field.classList.add("is-invalid");
            field.classList.remove("is-valid");
            errorSpan.textContent = `Invalid ${type} format`;
            return;
        }

        fetch(`/validate/?type=${type}&value=${encodeURIComponent(value)}`)
            .then(res => res.json())
            .then(data => {
                if (data.exists) {
                    field.classList.add("is-invalid");
                    field.classList.remove("is-valid");
                    errorSpan.textContent = `${type.charAt(0).toUpperCase() + type.slice(1)} already exists`;
                } else {
                    field.classList.remove("is-invalid");
                    field.classList.add("is-valid");
                    errorSpan.textContent = "";
                }
            });
    }

    for (const type in fields) {
        fields[type].addEventListener("blur", () => validateField(fields[type], type));
    }
});
