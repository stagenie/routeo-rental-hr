> 📘 **Code compagnon de l'ebook _« Développer sur Odoo 19 — Édition Routeo »_ — OdooSkills.**
> 👉 **[Obtenir l'ebook](https://odooskills.com/shop/formation-technique-odoo-19-ebook-3)** — le livre explique pas à pas tout le code de ce dépôt.

---

# Routeo Rental HR

Extension RH du module **Routeo Rental** : permet d'attacher un employé à un bon de location, calcule automatiquement la remise interne de 30 % sur le prix journalier, expose les filtres « Location interne » et « Mes équipes » dans la searchview.

## Dépendances

- `routeo_rental` (module de base)
- `hr` (Odoo natif)

## Installation

`./odoo-bin -c config/odoo.conf -i routeo_rental_hr -d <db>`

## Usage

1. Renseigner un employé sur un bon de location
2. Le bon est automatiquement marqué « Location interne »
3. Toutes ses lignes voient leur prix journalier réduit de 30 %
4. Les managers utilisent le filtre « Mes équipes » pour suivre les bons de leurs subordonnés directs

## Licence

LGPL-3