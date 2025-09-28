# 🔐 Cybersecurity Mini Projects

This repository contains beginner-friendly cybersecurity tasks
implemented in Python.\
Each task focuses on fundamental concepts in **cryptography, system
interaction, and data security**.

------------------------------------------------------------------------

## ✅ Task 01: Caesar Cipher

A Python script that implements a classic Caesar Cipher
encryption/decryption.

### Run

``` bash
python caesar_cipher.py
```

------------------------------------------------------------------------

## ✅ Task 02: Simple Image Encryption Tool

A Python script that implements a basic image cipher using the Pillow
(PIL) library.\
It encrypts and decrypts images by manipulating the **RGB pixel
values**.

### 🔧 Method

-   Uses **Bitwise XOR (⊕)** with a user-defined integer key.
-   Each Red, Green, and Blue channel value is XORed with the key.
-   The process is **reversible** (running XOR again with the same key
    decrypts the image).

### 📦 Prerequisites

``` bash
pip install Pillow
```

### Core Skills Demonstrated

-   Binary Operations\
-   Image Processing\
-   Data Integrity (via XOR reversibility)

### Run

``` bash
python img_cipher.py
```

------------------------------------------------------------------------

## 📝 Planned Tasks

### 🔑 Task 03: Password Strength Assessor

-   Assess passwords based on **complexity criteria** (length, character
    variety).

### ⌨️ Task 04: Basic Keylogger

-   Record keystrokes and log them to a file.\
-   Focus on **low-level system interaction**.

------------------------------------------------------------------------

## 🚀 Getting Started

1.  Clone the repository (if hosted on GitHub) or download the files.\
2.  Ensure Python 3 is installed.\
3.  Install dependencies:

``` bash
pip install Pillow
```

4.  Run tasks from the terminal:

``` bash
# To run Task 01
python caesar_cipher.py

# To run Task 02
python img_cipher.py
```

------------------------------------------------------------------------

## 📌 Author

Developed as part of **Cybersecurity Fundamentals Practice** 🚀
