// ==UserScript==
// @name         Phương Hòn Đá tải file MP3 trên trang thuvienhoclieu.com
// @namespace    http://tampermonkey.net/
// @version      2024-07-25
// @description  Tải file MP3 từ danh sách các file nghe có trên trang
// @author       Trần Minh Sáng (tmsanghoclaptrinh)
// @match        https://thuvienhoclieu.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=thuvienhoclieu.com
// @grant        GM_download
// @grant        GM_addStyle
// ==/UserScript==

(function() {
  'use strict';

  GM_addStyle(`
      @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

      .tms-button-cta {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 9999;
        padding: 1.2em 1rem;
        cursor: pointer;
        gap: 0.4rem;
        font-weight: bold;
        border-radius: 30px;
        text-shadow: 2px 2px 3px rgb(136 0 136 / 50%);
        background: linear-gradient(15deg, #880088, #aa2068, #cc3f47, #de6f3d, #f09f33, #de6f3d, #cc3f47, #aa2068, #880088) no-repeat;
        background-size: 300%;
        color: #fff;
        border: none;
        background-position: left center;
        box-shadow: 0 30px 10px -20px rgba(0,0,0,.2);
        transition: background .3s ease;
      }

      .tms-button-cta:hover {
        background-size: 320%;
        background-position: right center;
      }

      .tms-popup {
        position: fixed;
        top: 40%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: #1b1b32;
        color: #fff;
        border-radius: 8px;
        border: none;
        box-shadow: #ff596ccc 2px 1px 20px 11px;
        padding: 20px;
        z-index: 10000;
        width: 600px;
        height: 400px;
        overflow-y: auto;
        cursor: grab;
      }

      .tms-popup .tms-text-danger {
        margin-top: 40px;
        color: #e52b50;
      }

      .tms-popup ol {
        margin-top: 40px;
      }

      .tms-popup ol li {
        margin-bottom: 20px;
      }

      .tms-popup ol li span {
        margin-right: 20px;
      }

      .tms-popup .tms-download-button {
        background-color: transparent;
        color: #fff;
        border: 1px solid #ccc;
      }

      .tms-popup .tms-download-button:hover {
        opacity: 0.8;
      }

      .tms-popup .tms-close-button {
        position: absolute;
        top: 10px;
        right: 10px;
        color: #fff;
        background-color: transparent;
        border: none;
        outline: none;
        width: 32px;
        height: 32px;
      }
  `);

  let button = document.createElement('button');
  button.className = 'tms-button-cta';
  button.innerHTML = '<i class="fas fa-download" style="margin-right: 8px;"></i>Phương Hòn Đá tải file MP3 tại đây điii!!!';

  document.body.appendChild(button);

  button.addEventListener('click', function() {
      openPopup();
  });

  function openPopup() {
      let popup = document.createElement('div');
      popup.className = "tms-popup";

      const nodeList = document.querySelectorAll("audio.wp-audio-shortcode a");
      const listItems = [...nodeList];

      if (listItems.length === 0) {
          let h1Item = document.createElement('h1');
          h1Item.innerHTML = 'Không có file nghe nào trên trang này cả!!!';
          h1Item.className = 'text-danger';
          popup.appendChild(h1Item);
      }
      else {

          let orderedList = document.createElement('ol');
          let items = listItems.map((item) => {return {name: item.href.substring(item.href.lastIndexOf('/') + 1), url: item.href}});

          items.forEach(function(item) {
              let listItem = document.createElement('li');

              let itemName = document.createElement('span');
              itemName.innerHTML = item.name;

              let downloadButton = document.createElement('button');
              downloadButton.className = 'tms-download-button';
              downloadButton.innerHTML = '<i class="fas fa-download" style="margin-right: 8px;"></i>Download';
              downloadButton.addEventListener('click', function() {
                  downloadMP3(item.url, item.name + '.mp3');
              });

              listItem.appendChild(itemName);
              listItem.appendChild(downloadButton);
              orderedList.appendChild(listItem);
          });

          popup.appendChild(orderedList);
      }

      document.body.appendChild(popup);

      let closeButton = document.createElement('button');
      closeButton.className = "tms-close-button"
      closeButton.innerHTML = '<i class="fa-solid fa-xmark fa-xl" title="Close"></i>';

      closeButton.addEventListener('click', function() {
          document.body.removeChild(popup);
      });

      popup.appendChild(closeButton);

      dragElement(popup);
  }

  function dragElement(element) {
      let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;

      element.onmousedown = dragMouseDown;

      function dragMouseDown(e) {
          e = e || window.event;
          e.preventDefault();
          pos3 = e.clientX;
          pos4 = e.clientY;
          document.onmouseup = closeDragElement;
          document.onmousemove = elementDrag;
      }

      function elementDrag(e) {
          e = e || window.event;
          e.preventDefault();
          pos1 = pos3 - e.clientX;
          pos2 = pos4 - e.clientY;
          pos3 = e.clientX;
          pos4 = e.clientY;
          element.style.top = (element.offsetTop - pos2) + "px";
          element.style.left = (element.offsetLeft - pos1) + "px";
      }

      function closeDragElement() {
          document.onmouseup = null;
          document.onmousemove = null;
      }
  }

  function downloadMP3(url, filename) {
      GM_download({
          url: url,
          name: filename,
          onload: function() {
              console.log('Download complete: ' + filename);
          },
          onerror: function(error) {
              alert('Download failed: ' + filename + '\nError: ' + error.error + '\nDetails: ' + error.details);
          }
      });
  }
})();
