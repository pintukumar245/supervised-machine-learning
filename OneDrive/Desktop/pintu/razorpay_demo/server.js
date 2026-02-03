const express = require('express');
const Razorpay = require('razorpay');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const path = require('path');

const app = express();
app.use(bodyParser.json());
app.use(express.static('public'));

// Replace these with your actual Razorpay Key ID and Secret
const razorpay = new Razorpay({
    key_id: 'rzp_test_1DP5mmOlF5G5ag', // Test Key
    key_secret: 's4s4s4s4s4s4s4s4s4s4s4s4' // Dummy Secret (Use yours)
});

// Step 1: Create an Order
app.post('/create-order', async (req, res) => {
    const options = {
        amount: 50000, // Amount in paise (50000 paise = 500 INR)
        currency: 'INR',
        receipt: 'receipt_order_74394',
    };

    try {
        const order = await razorpay.orders.create(options);
        res.json(order);
    } catch (error) {
        console.error(error);
        res.status(500).send('Error creating order');
    }
});

// Step 2: Verify Payment
app.post('/verify-payment', (req, res) => {
    const { razorpay_order_id, razorpay_payment_id, razorpay_signature } = req.body;

    const sign = razorpay_order_id + "|" + razorpay_payment_id;
    const expectedSign = crypto
        .createHmac("sha256", razorpay.key_secret)
        .update(sign.toString())
        .digest("hex");

    if (razorpay_signature === expectedSign) {
        res.json({ status: 'success', message: 'Payment verified successfully' });
    } else {
        res.status(400).json({ status: 'failure', message: 'Invalid signature' });
    }
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
