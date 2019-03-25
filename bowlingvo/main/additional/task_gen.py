from .generators.base import *


def task_gen(lesson_id):
    generator = BaseGenerator()
    lesson = Lesson.objects.get(pk=lesson_id)
    sec = lesson.section
    if sec.sec_type == 'L':
        theory, tasks = generator.lex_tasks(lesson)
    else:
        theory, tasks = generator.gram_tasks(lesson)
    return theory, tasks
