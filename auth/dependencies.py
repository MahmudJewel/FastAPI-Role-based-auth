from fastapi import FastAPI, Depends, HTTPException
import auth

# Role based access control
class RoleChecker:
	def __init__(self, allowed_roles: list[str]):
		self.allowed_roles = allowed_roles

	# import auth
	def __call__(self, user: auth.schemas.User = Depends(auth.functions.get_current_user)):
		if user.role not in self.allowed_roles:
			# logger.debug(f"User with role {user.role} not in {self.allowed_roles}")
			raise HTTPException(status_code=403, detail="Operation not permitted")


