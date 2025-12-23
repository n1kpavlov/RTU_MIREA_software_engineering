package com.example.currency.controller;

import com.example.currency.model.User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller

public class AuthController {
    private User registedUser;
    private boolean isAuthenticated = false;

    @GetMapping("/")
    public String showRegisterPage() {
        return "register";
    }

    @PostMapping("/register")
    public String register(@RequestParam String username, @RequestParam String password, Model model) {
        if (username.isEmpty() || password.isEmpty()) {
            model.addAttribute("error", "Имя пользователя и пароль не должны быть пустыми!");
            return "register";
        }
        registedUser = new User(username, password);
        return "redirect:/login";
    }

    @GetMapping("/login")
    public String showLoginPage() {
        return "login";
    }

    @PostMapping("/login")
    public String login(@RequestParam String username, @RequestParam String password, Model model) {
        if (registedUser == null || !registedUser.getUsername().equals(username) || !registedUser.getPassword().equals(password)) {
            model.addAttribute("error", "Неверное имя пользователя или пароль!");
            return "login";
        }
        isAuthenticated = true;
        return "redirect:/home";
    }

    @GetMapping("/home")
    public String showHomePage(Model model) {
        if (!isAuthenticated) {
            return "redirect:/login";
        }

        model.addAttribute("username", registedUser.getUsername());
        return "home";
    }

    @PostMapping("/home")
    public String convert(@RequestParam String formType, @RequestParam double amount, @RequestParam String fromCurrency, @RequestParam String toCurrency, Model model) {
        if (!formType.equals("convert")) {
            return "home";
        }

        double result = 0;
        double value_1 = amount;
        String currency_1 = fromCurrency;
        String currency_2 = toCurrency;

        double rate = getExchangeRate(fromCurrency, toCurrency);
        result = amount * rate;

        model.addAttribute("username", registedUser.getUsername());
        model.addAttribute("value_1", value_1);
        model.addAttribute("currency_1", currency_1);
        model.addAttribute("value_2", result);
        model.addAttribute("currency_2", currency_2);
        return "home";
    }

    private double getExchangeRate(String from, String to) {
        if (from.equals("USD") && to.equals("RUB")) return 103.43;
        if (from.equals("USD") && to.equals("EUR")) return 0.95105;
        if (from.equals("EUR") && to.equals("RUB")) return 109.01;
        if (from.equals("EUR") && to.equals("USD")) return 1.05;
        if (from.equals("RUB") && to.equals("USD")) return 0.009668;
        if (from.equals("RUB") && to.equals("EUR")) return 0.009173;
        return 1;
    }
}
