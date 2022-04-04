import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

const HttpOptions = {
  headers : new HttpHeaders ({
    'Content-type': 'application/json',
  })
}

@Injectable({
  providedIn: 'root'
})
export class CurrenciesService {
  url: string = "http://localhost:8000/"; 

  startCurrency: String = '';
  targetCurrency: String = '';
  sequence: string[] = [];

  constructor(private http: HttpClient) { }
  
  sendCurrencies() {
    const currs = {
      "first": this.startCurrency,
      "second": this.targetCurrency
    }
    this.http.post<string[]>(this.url + "exchange", currs, HttpOptions).subscribe(
      (sequence: string[]) => {
        this.sequence = sequence;
      }
    )
  }

  getCurrencies() :Observable<string[]> {
    return this.http.get<string[]>(this.url + 'currencies', HttpOptions);
  }
}
