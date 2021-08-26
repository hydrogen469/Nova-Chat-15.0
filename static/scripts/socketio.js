document.addEventListener('DOMContentLoaded', () => {
  var socket = io();
  let room = "Social interactions and interests";
  joinRoom("Social interactions and interests");
  socket.on('message', data => {
    const p = document.createElement('p');
    const span_username = document.createElement('span');
    const span_timestamp = document.createElement('span');
    const br = document.createElement('br');
    if (data.username) {
      span_username.innerHTML = data.username;
      span_timestamp.innerHTML = data.time_stamp
      p.innerHTML = span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML;
      document.querySelector('#displaying-message-section').append(p);
    } else {
      printSysMsg(data.msg);
    }
  });
  
  document.querySelector('#send-message').onclick = () => {
    socket.send({'msg': document.querySelector('#user-message').value, 'username': username, 'room': room});
    document.querySelector('#user-message').value = '';
  }

  document.querySelectorAll('.select-room').forEach(p => {p.onclick = () => {
    let newRoom = p.innerHTML;
    if (newRoom == room) {
      msg = `You are already in the ${room} room.`
      printSysMsg(msg);
    } else {
      leaveRoom(room);
      joinRoom(newRoom);
      room = newRoom;
    }
  }
  });
  function leaveRoom(room) {
    socket.emit('leave', {'username': username, 'room': room});
  }
  function joinRoom(room) {
    socket.emit('join', {'username': username, 'room': room});
    document.querySelector('#displaying-message-section'),innerHTML = '';
    document.querySelector('#user-message').focus();
  }
  function printSysMsg(msg) {
    const p = document.createElement('p');
    p.innerHTML = msg;
    document.querySelector('#displaying-message-section').append(p);
  }
})