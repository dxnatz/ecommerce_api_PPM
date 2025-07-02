# 🛠️ Progetto E-Commerce API

Questo progetto è stato realizzato per l’insegnamento di **Progettazione e Produzione Multimediale**.

Si tratta di una **piattaforma e-commerce basata su Django** con un’API RESTful, pensata per la gestione di prodotti, carrelli, ordini e autenticazione degli utenti.

---

## ⚙️ Tecnologie utilizzate

- **Python** – Logica backend e gestione dei dati
- **HTML** – Creare una semplice e minimale interfaccia per l'utente
- **JavaScript (fetch API)** – Comunicazione con il backend

## 🔐 Autenticazione

L’autenticazione è gestita tramite **JSON Web Token (JWT)** usando il pacchetto `SimpleJWT`.  
Gli utenti devono effettuare il login per accedere alle funzionalità protette come visualizzare i prodotti, il carrello ed effettuare il checkout.

## 🛒 Funzionalità disponibili

### 🛍️ Frontend (accessibile a tutti)

- Registrazione e login utenti  
- Visualizzazione prodotti  
- Aggiunta prodotti al carrello  
- Rimozione prodotti dal carrello  
- Checkout ordine (senza pagamento)

### 🛠️ Backend (pannello admin Django)

- Aggiungi / modifica / elimina:
    - prodotti
    - ordini e articoli dell'ordine
    - carrelli e articoli del carrello
    - utenti
- Gestisci gli sconti sugli articoli
- Assegni o rimuovi ruoli utenti (ad esempio **moderatore** oppure **responsabile prodotti**)  
- Bannare / sbannare utenti  
- Accesso completo a tutti i dati e modelli

## 👥 Ruoli utente e permessi

I ruoli sono gestiti con il sistema **Group & Permissions** integrato in Django.

### 👑 Superuser
I **superuser** hanno pieno accesso all'intero backend tramite l'interfaccia di amministrazione di Django.  
Possono gestire tutti i modelli, gli utenti e le autorizzazioni senza restrizioni.

### 🛡️ Moderatore
I **moderatori** hanno accesso a:

- Visualizzare tutti i prodotti
- Aggiungi / modifica / elimina:
  - ordini e articoli dell'ordine
  - carrelli e articoli del carrello
  - utenti (senza però modificare i vari permessi, ovvero supersuser status, staff status e active)

### 📦 Responsabile prodotti
I **responsabili prodotti** hanno accesso a:

- Visualizzare tutti gli ordini e articoli dell'ordine, i carrelli e articoli del carrello e gli utenti
- Aggiungi / modifica / elimina:
  - Prodotti

## 🔐 Account di test (pannello admin)

Per testare i diversi ruoli e i relativi permessi è possibile utilizzare i seguenti account pre-registrati:

| Ruolo              | Username      | Password     |
|--------------------|---------------|--------------|
| Superuser          | `mattia`      | `passmat123` |
| Moderatore         | `gabriele`    | `passgab123` |
| Responsabile prodotti   | `filippo`     | `passfil123` |
| Utente Normale     | `martino`     | `passmar123` |

## 🧪 Come testare le funzionalità del backend

Tutte le funzionalità di backend possono essere testate accedendo al **pannello di amministrazione di Django** all'indirizzo `https://ecommerceapippm.up.railway.app/admin/` utilizzando le credenziali fornite sopra.
Una volta effettuato l'accesso, ogni utente vedrà solo le sezioni e le azioni consentite dal proprio ruolo.

Ricordo che **gli utenti normali non hanno accesso al pannello di amministrazione del backend** e possono utilizzare solo le funzionalità del frontend.
Solo gli account Superuser, Moderatore e Responsabile prodotti hanno accesso al backend con diversi livelli di autorizzazione.

## 🚀 Deploy

Il progetto è stato deployato su **Railway**.
Come database ho usato **PostgreSQL** fornito all'interno di Railway.

### 🌍 URL produzione

Frontend HTML:  
👉 `https://ecommerceapippm.up.railway.app/`  

Backend API:  
👉 `https://ecommerceapippm.up.railway.app/admin/`
