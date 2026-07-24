import uuid
from typing import Optional
from fastapi import Depends, Request
from fastapi_users import FastAPIUsers, BaseUserManager, UUIDIDMixin, models