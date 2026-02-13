{% extends "base.html" %}
{% block content %}

<h2 class="text-2xl font-bold mb-4">Quiz</h2>

<div id="quiz">
{% for q in quiz %}
  <div class="bg-white p-6 rounded-2xl shadow mb-4">
    <p class="font-semibold">{{ q.question }}</p>
    {% for opt in q.options %}
      <button
        onclick="checkAnswer(this, '{{ opt }}', '{{ q.answer }}')"
        class="block w-full text-left border p-2 rounded-xl mt-2">
        {{ opt }}
      </button>
    {% endfor %}
  </div>
{% endfor %}
</div>

<script src="/static/quiz.js"></script>
{% endblock %}
