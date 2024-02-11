if (
  localStorage.theme === "dark" ||
  (!("theme" in localStorage) &&
    window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  document.documentElement.classList.add("dark");
  document.getElementById("light-mode-toggle").style.display = "block";
  document.getElementById("dark-mode-toggle").style.display = "none";
} else {
  document.documentElement.classList.remove("dark");
  document.getElementById("dark-mode-toggle").style.display = "block";
  document.getElementById("light-mode-toggle").style.display = "none";
}

function toggleDarkMode() {
  document.documentElement.classList.add("dark");
  localStorage.theme = "dark";
  document.getElementById("light-mode-toggle").style.display = "block";
  document.getElementById("dark-mode-toggle").style.display = "none";
}

function toggleLightMode() {
  document.documentElement.classList.remove("dark");
  localStorage.theme = "light";
  document.getElementById("dark-mode-toggle").style.display = "block";
  document.getElementById("light-mode-toggle").style.display = "none";
}
