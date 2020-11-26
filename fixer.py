from datacenter.models import Schoolkid, Mark, Chastisement, Commendation, Lesson, Subject
import random

COMMENDATIONS = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"
]


def fix_marks(schoolkid):
    """Change points 1, 2, 3 to 5."""
    Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)


def remove_chastisements(schoolkid):
    """Remove all chastisements for schoolkid."""
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid: Schoolkid, subject: Subject.title):
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    subject = Subject.objects.get(title=subject, year_of_study=year_of_study)

    lesson = Lesson.objects.filter(
        year_of_study=year_of_study,
        group_letter=group_letter,
        subject=subject
    ).order_by('date').last()

    Commendation.objects.create(
        text=random.choice(COMMENDATIONS),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher
    )
