from rest_framework import serializers

from account.models import User
from contacts.models import Contact, Spam


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("external_id", "name", "phone")


class ContactListWithSpamSerializer(ContactListSerializer):
    spam_count = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ContactListSerializer.Meta.fields + ("spam_count",)

    def get_spam_count(self, obj: Contact) -> int:
        return Spam.objects.filter(phone=obj.phone).count()
