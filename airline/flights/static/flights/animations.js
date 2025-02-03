const spotlight = document.querySelector('.spotlight');

        document.addEventListener('mousemove', (e) => {
            spotlight.style.transform = `translate(${e.clientX - 100}px, ${e.clientY - 100}px)`;
        });