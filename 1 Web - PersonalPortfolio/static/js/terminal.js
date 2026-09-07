const visual = document.querySelector(".inicio-visual");
const terminal = document.querySelector(".terminal");

if (visual && terminal) {

    visual.addEventListener("mousemove", (event) => {

        const rect = visual.getBoundingClientRect();

        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / centerY) * -3;
        const rotateY = ((x - centerX) / centerX) * 3;

        terminal.style.transform = `
            perspective(800px)
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
        `;
    });


    visual.addEventListener("mouseleave", () => {

        terminal.style.transform = `
            perspective(800px)
            rotateX(0deg)
            rotateY(0deg)
        `;
    });
}
