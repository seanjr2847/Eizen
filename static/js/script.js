
  function removeTask(button) {
    button.parentElement.remove();
  }

  function allowDrop(event) {
    event.preventDefault();
  }

  function drag(event) {
    event.dataTransfer.setData("text", event.target.getAttribute('data-task'));
  }

  function drop(event) {
    event.preventDefault();
    var data = event.dataTransfer.getData("text");
    var task = document.querySelector(`[data-task="${data}"]`);
    if (task) {
      event.target.closest('.matrix-quadrant, .undecided-area').appendChild(task);
    }
  }

  document.getElementById('create-task').addEventListener('click', () => {
    const taskName = prompt('작업의 이름을 입력해주세요.');
    if (taskName) {
      const newTask = document.createElement('div');
      newTask.classList.add('task-card', 'draggable');
      newTask.setAttribute('draggable', 'true');
      newTask.setAttribute('data-task', taskName.replace(/\s+/g, '-').toLowerCase());
      newTask.setAttribute('ondragstart', 'drag(event)');
      newTask.innerHTML = `<span>${taskName}</span><button class="done-button" onclick="removeTask(this)">완료</button>`;
      document.querySelector('.undecided-area').appendChild(newTask);
    }
  })

  document.addEventListener('DOMContentLoaded', function () {
    const tabs = document.querySelectorAll('#tabs li');
    const tabContents = document.querySelectorAll('.tab-content');
  
    tabs.forEach(tab => {
      tab.addEventListener('click', function (e) {
        e.preventDefault();
  
        const targetId = this.getAttribute('data-target');
        const targetContent = document.getElementById(targetId);
  
        tabContents.forEach(tc => {
          tc.classList.add('hidden');
        });
  
        tabs.forEach(t => {
          t.children[0].classList.remove('text-blue-600', 'border-blue-600');
          t.children[0].classList.add('text-gray-500', 'border-transparent');
        });
  
        this.children[0].classList.add('text-blue-600', 'border-blue-600');
        this.children[0].classList.remove('text-gray-500', 'border-transparent');
  
        targetContent.classList.remove('hidden');
      });
    });
  });
