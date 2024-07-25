// ==UserScript==
// @name         Phương Hòn Đá tải file MP3 trên trang thuvienhoclieu.com
// @namespace    http://tampermonkey.net/
// @version      2024-07-25
// @description  Tải file MP3 từ danh sách các file nghe có trên trang
// @author       Trần Minh Sáng (tmsanghoclaptrinh)
// @match        https://thuvienhoclieu.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=thuvienhoclieu.com
// @grant        GM_download
// ==/UserScript==

(function() {
    'use strict';

    let button = document.createElement('button');
    button.innerHTML = 'Phương Hòn Đá tải file MP3 tại đây điii!!!';
    button.style.position = 'fixed';
    button.style.top = '10px';
    button.style.right = '10px';
    button.style.zIndex = '9999';
    button.style.width = '400px';
    button.style.height = '50px';
    button.style.backgroundColor = 'green';
    button.style.color = '#fff';
    button.style.fontWeight = 'bold';
    document.body.appendChild(button);

    button.addEventListener('click', function() {
        openPopup();
    });

    function openPopup() {
        let popup = document.createElement('div');
        popup.style.position = 'fixed';
        popup.style.top = '30%';
        popup.style.left = '50%';
        popup.style.transform = 'translate(-50%, -50%)';
        popup.style.backgroundColor = '#1b1b32';
        popup.style.color = '#fff';
        popup.style.border = '1px solid #ccc';
        popup.style.borderRadius = '8px';
        popup.style.boxShadow = 'rgba(0, 0, 0, 0.35) 20px 13px 50px 20px';
        popup.style.padding = '20px';
        popup.style.zIndex = '10000';
        popup.style.width = '600px';
        popup.style.height = '400px';
        popup.style.overflowY = 'auto';
        popup.style.cursor = "grab";

        let orderedList = document.createElement('ol');
        orderedList.style.marginTop = '40px';
        const nodeList = document.querySelectorAll("audio.wp-audio-shortcode a");
        const listItems = [...nodeList];
        let items = listItems.map((item) => {return {name: item.href.substring(item.href.lastIndexOf('/') + 1), url: item.href}});

        items.forEach(function(item) {
            let listItem = document.createElement('li');
            listItem.style.marginBottom = '10px';

            let itemName = document.createElement('span');
            itemName.innerHTML = item.name;
            itemName.style.marginRight = '10px';

            let downloadButton = document.createElement('button');
            downloadButton.innerHTML = 'Download';
            downloadButton.style.backgroundColor = '#1b1b32';
            downloadButton.style.color = '#fff';
            downloadButton.style.border = '1px solid #ccc';
            downloadButton.addEventListener('click', function() {
                downloadMP3(item.url, item.name + '.mp3');
            });

            listItem.appendChild(itemName);
            listItem.appendChild(downloadButton);
            orderedList.appendChild(listItem);
        });

        popup.appendChild(orderedList);

        document.body.appendChild(popup);

        let closeButton = document.createElement('button');
        closeButton.innerHTML = 'Close';
        closeButton.style.position = 'absolute';
        closeButton.style.top = '10px';
        closeButton.style.right = '10px';
        closeButton.style.backgroundColor = '#1b1b32';
        closeButton.style.color = '#fff';
        closeButton.style.border = '1px solid #ccc';
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
