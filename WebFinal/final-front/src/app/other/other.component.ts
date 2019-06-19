import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';

@Component({
  selector: 'app-other',
  templateUrl: './other.component.html',
  styleUrls: ['./other.component.scss']
})
export class OtherComponent implements OnInit {

  public message = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {

    this.provider.sendMessage.subscribe(res => {
      this.message = res;
    });

  }

}
