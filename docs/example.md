# Invoice-approval example

Actual output from a `show-shape` run, rendered by Radian’s native terminal harness. The screenshot is cropped to show the response and composer, without the performance footer.

## Agreed design

A fictitious accounts-payable console for Acme Studio. The approver reviews Northstar Labs invoice INV-1048 for EUR 12,480, due 6 Oct. Workspace navigation and a filtered inbox sit beside the original PDF, verified purchase-order/tax checks, and the approval chain (Ava completed stage 1, You are assigned stage 2). Actions are Request changes and Approve.

The client owns temporary drafts and preview presentation. The Invoice API owns tenant, approver, state, version, and idempotency checks. A rejection leaves the invoice unchanged. Postgres commits Approved status, actor/time audit, and an export-outbox event atomically. A worker performs retry-safe ERP export, not payment. The private original PDF is unchanged and accessed through an API-authorized signed URL.

## Request

Use show-shape to draw the agreed invoice-approval console. Show the screen and ownership path, including the approver/version gate, unchanged rejection path, atomic audit/outbox commit, and retry-safe ERP export. Keep the two views together within about 40 diagram lines and 100 columns. Use the actual invoice, vendor, amount, and approver names from our discussion. Do not redesign or edit files.

The follow-up requests tightened the two views to 15/17 diagram lines, checked fixed-width alignment, and restored Unicode box-drawing borders while preserving the design.

## Response

### screen
Actions target INV-1048. Approval accepts accounting export, not payment. States use text and icons.
```text
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│ Acme Studio / Invoice approval                                                               │
├─────────────┬──────────────────┬────────────────────────────────────────┬────────────────────┤
│ Workspace   │ Invoice inbox    │ Selected invoice review                │ Approval / activity│
│ > Inbox     │ Pending approval │ Northstar Labs / INV-1048               │ [ok] Ava - stage 1 │
│   Vendors   │ Approved         │ EUR 12,480 / Due 6 Oct                  │ [>] You - stage 2  │
│   Audit log │ Needs changes    │ [>] Pending approval                   │ Assigned approver  │
│             │ > INV-1048       │ ┌─ Original PDF ──┬─ Verified ───────┐ │ Recent activity    │
│             │ Northstar Labs   │ │ Rendered page   │ Northstar Labs   │ │ Ava approved       │
│             │ EUR 12,480       │ │ INV-1048        │ [ok] PO match    │ │                    │
│             │ Due 6 Oct        │ │ EUR 12,480      │ [ok] Tax check   │ │                    │
│             │   INV-1047       │ │                 │ EUR 12,480 total │ │                    │
│             │   INV-1046       │ └─────────────────┴──────────────────┘ │                    │
│             │                  │ [Request changes]  [Approve]           │                    │
└─────────────┴──────────────────┴────────────────────────────────────────┴────────────────────┘
```

### ownership
Private PDF: API-gated signed URL. Keys/races deduplicated. ERP outage preserves approval/audit.
```text
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│ Client: temporary selection / drafts / PDF preview                                            │
└──────────────────┬───────────────────────────────────────────────────────────────────────────┘
                   ▼ Approve: INV-1048 + reviewed version + idempotency key + actor token
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│ Invoice API: tenant scope / Pending approval / Ava stage complete                             │
│ Server gate: Assigned approver + current version? (You, stage 2)                              │
└──────────────────┬──────────────────────────────────────────────┬────────────────────────────┘
                   ▼ YES                                          ▼ NO
┌─ Postgres ────────────────────────────────────┐  ┌─ Rejected ────────────────────────────────┐
│ Atomic: Approved + actor/time audit            │  │ Unapproved / no success writes or export  │
│ + export-outbox event, ONE transaction         │  │ 403 denied / 409 stale -> reload review   │
└───────────────────────────────────────────────┘  └───────────────────────────────────────────┘
                   ▼ committed outbox
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│ Export worker -> ERP adapter / retry-safe + deduplicated / no payment                         │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```
