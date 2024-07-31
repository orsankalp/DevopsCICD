from django.test import SimpleTestCase
from playground.forms import BookingForm, contactForm, DateInput

class FormTestCase(SimpleTestCase):
    def test_booking_form_date_widgets(self):
        # Test if the period_from and period_to fields of BookingForm have DateInput widgets
        form = BookingForm()
        self.assertIsInstance(form.fields['period_from'].widget, DateInput)
        self.assertIsInstance(form.fields['period_to'].widget, DateInput)

    def test_contact_form_fields(self):
        # Test if all fields of contactForm are included in the form
        form = contactForm()
        self.assertEqual(form.fields.keys(), {'client_id', 'client_phone', 'client_problem'})

    # Add more tests as needed
