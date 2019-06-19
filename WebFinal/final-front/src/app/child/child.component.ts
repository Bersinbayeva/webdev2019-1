import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.scss']
})
export class ChildComponent implements OnInit {

  @Input() title = '';
  @Input() numberArray: number[] = [];

  @Output() output = new EventEmitter();
  @Output() stringArray = new EventEmitter<string[]>();

  constructor() { }

  ngOnInit() {
  }

  sendMessage() {
    this.output.emit('Message from Child');
  }

  sendStringArray() {
    this.stringArray.emit(['a', 'b', 'c']);
  }

}
