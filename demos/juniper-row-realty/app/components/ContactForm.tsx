"use client";
import {FormEvent,useState} from 'react';
export default function ContactForm(){
 const [done,setDone]=useState(false);
 function submit(e:FormEvent){e.preventDefault();setDone(true)}
 return <form className="contactForm" onSubmit={submit}><label>Name<input required autoComplete="name"/></label><label>Email<input required type="email" autoComplete="email"/></label><label>I am<select><option>Buying</option><option>Selling</option><option>Exploring both</option><option>Relocating</option></select></label><label>What matters most?<textarea rows={5} placeholder="Area, timing, price range, must-haves, or current property details"/></label><button className="button" type="submit">Send introduction</button>{done&&<p className="status" role="status">Demo inquiry complete. No real lead was submitted.</p>}</form>
}